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
