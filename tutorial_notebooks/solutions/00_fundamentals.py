"""
Exercise: <font color='red'>(⏰ 5 min) Define a function that
takes as input an RGB image and a pair of coordinates (row,
column), and returns a copy with a green letter H overlaid at
those coordinates. The coordinates point to the top-left corner
of the H.

The arms and strut of the H should have a width of 3 pixels,
and the H itself should have a height of 24 pixels and width of
20 pixels.

Start with the following template:

def draw_H(image, coords, color=(0, 255, 0)):
    image_with_H = image.copy()

    ...

    return image_with_H
"""

def draw_H(image, coords, color=(0, 255, 0)):
    """
    Draws the letter H within an input image.
    """
    image_with_H = image.copy()

    canvas = image_with_H[coords[0]:coords[0] + 24,
                          coords[1]:coords[1] + 20]

    canvas[:, :3] = color
    canvas[:, -3:] = color
    canvas[11:14] = color

    return image_with_H

"""
Exercise: (⏰ 5 min) Display the different color channels of `chelsea`
along, each as a gray-scale image.
"""

chelsea = data.chelsea()

# First, assign each color channel to a different variable.
channel_r = chelsea[:, :, 0]
channel_g = chelsea[:, :, 1]
channel_b = chelsea[:, :, 2]

# Then, display the image and the red, green and blue channels.
_, (ax_r, ax_g, ax_b, ax_color) = plt.subplots(nrows=1, ncols=4, figsize=(16, 5))

ax_r.imshow(channel_r, cmap='gray')
ax_r.set_title('Red channel')
ax_r.axis('off')

ax_g.imshow(channel_g, cmap='gray')
ax_g.set_title('Green channel')
ax_g.axis('off')

ax_b.imshow(channel_b, cmap='gray')
ax_b.set_title('Blue channel')
ax_b.axis('off')

# Here we rebuild the color image stacking the R, G, and B layers again.
ax_color.imshow(np.stack([channel_r, channel_g, channel_b], axis=2))
ax_color.set_title('All channels');
ax_color.axis('off')
