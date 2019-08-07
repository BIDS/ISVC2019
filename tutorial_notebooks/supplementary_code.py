import matplotlib.pyplot as plt
import numpy as np

from ipywidgets import interact
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scipy import stats
from skimage import exposure, io


def show_plane(axis, plane, cmap="gray", title=None):
    """Shows a specific plane within 3D data.
    """
    axis.imshow(plane, cmap=cmap)
    axis.set_xticks([])
    axis.set_yticks([])

    if title:
        axis.set_title(title)

    return None


def slice_in_3D(axis, shape, plane):
    """Draws a cube in a 3D plot.

    Notes
    -----
    Originally from:
    https://stackoverflow.com/questions/44881885/python-draw-parallelepiped
    """
    Z = np.array([[0, 0, 0],
                  [1, 0, 0],
                  [1, 1, 0],
                  [0, 1, 0],
                  [0, 0, 1],
                  [1, 0, 1],
                  [1, 1, 1],
                  [0, 1, 1]])

    Z = Z * shape

    r = [-1, 1]

    X, Y = np.meshgrid(r, r)

    # plotting vertices
    axis.scatter3D(Z[:, 0], Z[:, 1], Z[:, 2])

    # list of sides' polygons of figure
    verts = [[Z[0], Z[1], Z[2], Z[3]],
             [Z[4], Z[5], Z[6], Z[7]],
             [Z[0], Z[1], Z[5], Z[4]],
             [Z[2], Z[3], Z[7], Z[6]],
             [Z[1], Z[2], Z[6], Z[5]],
             [Z[4], Z[7], Z[3], Z[0]],
             [Z[2], Z[3], Z[7], Z[6]]]

    # plotting sides
    axis.add_collection3d(
        Poly3DCollection(verts,
                         facecolors=(0, 1, 1, 0.25),
                         linewidths=1,
                         edgecolors='darkblue')
    )

    verts = np.array([[[0, 0, 0],
                       [0, 0, 1],
                       [0, 1, 1],
                       [0, 1, 0]]])
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

    # auto-scale plot axes
    scaling = np.array([getattr(axis, 'get_{}lim'.format(dim))() for dim in 'xyz'])
    axis.auto_scale_xyz(*[[np.min(scaling), np.max(scaling)]] * 3)

    return None


def slice_explorer(data, cmap='gray'):
    N = len(data)

    @interact(plane=(0, N - 1))
    def display_slice(plane=34):
        fig, axis = plt.subplots(figsize=(20, 5))
        axis_3D = fig.add_subplot(133, projection='3d')
        show_plane(axis, data[plane], title=f'Plane {plane}', cmap=cmap)
        slice_in_3D(axis=axis_3D, shape=data.shape, plane=plane)

        plt.show()

    return display_slice


def display(data, cmap="gray", step=2):
    _, axes = plt.subplots(nrows=5, ncols=6, figsize=(16, 14))

    # getting data min and max to plot limits
    vmin, vmax = data.min(), data.max()

    for axis, image in zip(axes.flatten(), data[::step]):
        axis.imshow(image, cmap=cmap, vmin=vmin, vmax=vmax)
        axis.set_xticks([])
        axis.set_yticks([])

    return None


def plot_hist(axis, data, title=None):
    """Helper function for plotting histograms.
    """
    axis.hist(data.ravel(), bins=256)
    axis.ticklabel_format(axis='y', style='scientific', scilimits=(0, 0))

    if title:
        axis.set_title(title)

    return None



def results_from_part_1():

    data = io.imread("images/cells.tif")

    vmin, vmax = stats.scoreatpercentile(data, (0.5, 99.5))
    rescaled = exposure.rescale_intensity(
        data,
        in_range=(vmin, vmax),
        out_range=np.float32
    )

    equalized = exposure.equalize_hist(data)

    return data, rescaled, equalized
