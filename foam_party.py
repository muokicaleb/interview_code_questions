"""
Foam party in my garage!
My parents authorized me to throw a foam party in the garage.

I need to calculate the room’s volume, so I buy the appropriate quantity of foam liquid. Too much would be messy, and too few would not be fun.

But my dumb parents kept two stupid cardboard boxes in the garage and forbade me to move them. So it decreases the available fun volume!

Since they are obsessed with cleaning and order, the sides of the cardboard boxes are perfectly aligned with the garage walls and ground, and everything is perfectly rectangular. They tried to put one box into the other but may not have done it completely (as they are dumb).

I know my garage’s dimensions (width, length, height). I also measured the position of the two boxes (coordinates x, y, z, of two opposite corners of each box).

The 3 dimensions are always in the same order for every coordinate and size. They are float values.

The two boxes are always entirely contained in the garage. One may completely, partly, or not be contained in the other. My parents closed them with duct tape and paper so no foam could enter them. (Yes, they managed to pack a box that partly contains another box, don’t ask me how they did that, I don’t care).

Can you help me calculate the volume available for the foam?
"""

import numpy as np


garage_width = 5.0
garage_length = 6.0
garage_height = 3.0


box1_corner1 = np.array([1.0, 1.0, 1.0])  
box1_corner2 = np.array([2.0, 3.0, 2.0])  

box2_corner1 = np.array([3.0, 1.5, 0.5])  
box2_corner2 = np.array([4.5, 2.5, 1.5])  


def box_volume(corner1, corner2):
    return np.abs(np.prod(corner2 - corner1))

def garage_volume(width, length, height):
    return width * length * height

g_volume = garage_volume(garage_width, garage_length, garage_height)
box1_volume = box_volume(box1_corner1, box1_corner2)
box2_volume = box_volume(box2_corner1, box2_corner2)

available_foam_volume = g_volume - (box1_volume + box2_volume)

print(available_foam_volume)
