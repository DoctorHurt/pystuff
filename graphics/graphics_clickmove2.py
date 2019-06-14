"""
Testing ways to move an object around the screen using mouse clicks.
"""

from graphics import *

win = GraphWin("My Window", 800, 800)
win.setBackground('grey')

cir = Circle(Point(400, 400), 30)
cir.setFill('red')
cir.draw(win)

while True:
    m = win.getMouse()
    xcoord = int(m.getX())
    ycoord = int(m.getY())
    wherex = int(cir.getCenter().getX())
    wherey = int(cir.getCenter().getY())
    movex = xcoord - wherex
    movey = ycoord - wherey

    if movex > 0:
        xrange = range(1, movex, 1)
    else:
        xrange = range(1, movex, -1)

    if movey > 0:
        yrange = range(1, movey, 1)
    else:
        yrange = range(1, movey, -1)
    print(movex, movey)
    cir.move(movex, movey)
