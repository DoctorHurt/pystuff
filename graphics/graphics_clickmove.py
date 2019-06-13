"""
Testing ways to move an object around the screen using mouse clicks.
"""

from graphics import *

win = GraphWin("My Window", 800, 800)
win.setBackground('grey')

cir = Circle (Point(400, 400), 30)
cir.setFill('red')
cir.draw(win)

while True:
    m = win.getMouse()
    xcoord = int(m.getX())
    ycoord = int(m.getY())
    where = cir.getCenter()
    wherex = where.getX()
    wherey = where.getY()
    movex = int(xcoord - wherex)
    movey = int(ycoord - wherey)

    if movex > 0:
        xrange = range(1, movex, 1)
    else:
        xrange = range(1, movex, -1)

    if movey > 0:
        yrange = range(1, movey, 1)
    else:
        yrange = range(1, movey, -1)

    for x in xrange:
        print(f"x is: {x}")
        if movex > 0:
            cir.move(1, 0)
        else:
            cir.move(-1, 0)

    for y in yrange:
        print(f"y is: {y}")
        if movey > 0:
            cir.move(0, 1)
        else:
            cir.move(0, -1)
