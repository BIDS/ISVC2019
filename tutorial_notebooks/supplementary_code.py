import matplotlib.pyplot as plt
import numpy as np

from ipywidgets import interact
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def show_plane(axis, plane, cmap="gray", title=None):
    axis.imshow(plane, cmap=cmap)
    axis.set_xticks([])
    axis.set_yticks([])

    if title:
        axis.set_title(title)

    return None


def slice_in_3D(axis, shape, plane):
    '''Draws a cube in a 3D structure.

    Notes
    -----
    Originally from:
    https://stackoverflow.com/questions/44881885/python-draw-parallelepiped
    '''

    Z = np.array([[0, 0, 0],
                  [1, 0, 0],
                  [1, 1, 0],
                  [1, 0, 1],
                  [0, 1, 0],
                  [0, 1, 1],
                  [0, 0, 1],
                  [1, 1, 1]])

    Z = Z * shape

    r = [-1, 1]

    X, Y = np.meshgrid(r, r)
    # plot vertices
    axis.scatter3D(Z[:, 0], Z[:, 1], Z[:, 2])

    # list of sides' polygons of figure
    verts = [[Z[0], Z[1], Z[2], Z[3]],
             [Z[4], Z[5], Z[6], Z[7]],
             [Z[0], Z[1], Z[5], Z[4]],
             [Z[2], Z[3], Z[7], Z[6]],
             [Z[1], Z[2], Z[6], Z[5]],
             [Z[4], Z[7], Z[3], Z[0]],
             [Z[2], Z[3], Z[7], Z[6]]]

    # plot sides
    axis.add_collection3d(
        Poly3DCollection(verts,
                         facecolors=(0, 1, 1, 0.25),
                         linewidths=1,
                         edgecolors='darkblue')
    )

    verts = np.array([[[0, 0, 0],
                       [0, 1, 0],
                       [0, 0, 1],
                       [0, 1, 1]]])

    verts = verts * (60, 256, 256)
    verts += [plane, 0, 0]

    axis.add_collection3d(
        Poly3DCollection(verts,
                         facecolors='magenta',
                         linewidths=1,
                         edgecolors='black')
    )

    axis.set_xlabel('plane')
    axis.set_ylabel('col')
    axis.set_zlabel('row')

    # Auto-scale plot axes
    scaling = np.array([getattr(axis, 'get_{}lim'.format(dim))() for dim in 'xyz'])
    axis.auto_scale_xyz(*[[np.min(scaling), np.max(scaling)]] * 3)

    return None


def slice_explorer(data, cmap='gray'):
    N = len(data)

    @interact(plane=(0, N - 1))
    def display_slice(plane=34):
        fig, ax = plt.subplots(figsize=(20, 5))

        ax_3D = fig.add_subplot(133, projection='3d')

        show_plane(axis, data[plane], title="Plane {}".format(plane), cmap=cmap)
        slice_in_3D(ax_3D, plane)

        plt.show()

    return display_slice


def display(im3d, cmap="gray", step=2):
    _, axes = plt.subplots(nrows=5, ncols=6, figsize=(16, 14))

    vmin = im3d.min()
    vmax = im3d.max()

    for axis, image in zip(axes.flatten(), im3d[::step]):
        axis.imshow(image, cmap=cmap, vmin=vmin, vmax=vmax)
        axis.set_xticks([])
        axis.set_yticks([])

    return None


def plot_hist(axis, data, title=None):
    axis.hist(data.ravel(), bins=256)
    axis.ticklabel_format(axis="y", style="scientific", scilimits=(0, 0))

    if title:
        axis.set_title(title)

    return None
