""" Draw a square matrix spiral using randomly colored circles """

from graphics import *
import random

win = GraphWin("My Window", 800, 800)
win.setBackground(color_rgb(50, 50, 50))

def spiral(N, M):
    x,y = 0,0
    dx, dy = 0, -1
    for dumb in range(N*M):
        if abs(x) == abs(y) and [dx,dy] != [1,0] or x>0 and y == 1-x:
            dx, dy = -dy, dx            # corner, change direction
        if abs(x)>N/2 or abs(y)>M/2:    # non-square
            dx, dy = -dy, dx            # change direction
            x, y = -y+dx, x+dy          # jump
        yield x*8, y*8
        x, y = x+dx, y+dy

for a,b in spiral(80,80):
    rcolor = (random.randint(0, 255))
    gcolor = (random.randint(0, 255))
    bcolor = (random.randint(0, 255))
    size = (random.randint(10, 50))
    pt = Point(a + 400, b + 400)
    cir = Circle(pt, 10)
    cir.setFill(color_rgb(rcolor, gcolor, bcolor))
    cir.draw(win)

win.getMouse() # Pause to view result
win.close()    # Close window when done
