from graphics import *
import math
import sys
import random

win = GraphWin("My Window", 800, 800)
win.setBackground(color_rgb(50, 50, 50))

def spiral(radius, step, resolution=.1, angle=0.0, start=0.0):
    """
Spiral generator.
Inputs:
Radius - maximum radius of the spiral from the center.
  Defines the distance of the tail end from the center.
Step - amount the current radius increases between each point.
  Larger = spiral expands faster
Resolution - distance between 2 points on the curve.
  Defines amount radius rotates between each point.
  Larger = smoother curves, more points, longer time to calculate.
Angle - starting angle the pointer starts at on the interior
Start - starting distance the radius is from the center.
"""
    dist = start+0.0
    coords=[]
    while dist*math.hypot(math.cos(angle),math.sin(angle))<radius:
        cord=[]
        cord.append(dist*math.cos(angle))
        cord.append(dist*math.sin(angle))
        coords.append(cord)
        dist+=step
        angle+=resolution
    return coords

for a,b in spiral(800, .1, 1, 20.0):
    rcolor = (random.randint(0, 255))
    gcolor = (random.randint(0, 255))
    bcolor = (random.randint(0, 255))
    size = (random.randint(10, 50))
    pt = Point(a + 400, b + 400)
    cir = Circle(pt, 50)
    cir.setFill(color_rgb(rcolor, gcolor, bcolor))
    cir.draw(win)

win.getMouse() # Pause to view result
win.close()    # Close window when done
