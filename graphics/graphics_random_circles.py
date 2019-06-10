from graphics import *
import random

win = GraphWin("My Window", 800, 800)
win.setBackground(color_rgb(50, 50, 50))

count = 0
while count < 3000:
    xcord = (random.randint(0, 801))
    ycord = (random.randint(0, 801))
    rcolor = (random.randint(0, 255))
    gcolor = (random.randint(0, 255))
    bcolor = (random.randint(0, 255))
    size = (random.randint(10, 50))

    pt = Point(xcord, ycord)
    cir = Circle(pt, size)
    cir.setFill(color_rgb(rcolor, gcolor, bcolor))
    cir.draw(win)
    count += 1

win.getMouse() # Pause to view result
win.close()    # Close window when done
