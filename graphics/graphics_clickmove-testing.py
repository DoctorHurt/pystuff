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
    wherex = int(cir.getCenter().getX())
    wherey = int(cir.getCenter().getY())
    movex = int(xcoord - wherex)
    movey = int(ycoord - wherey)

    if movex > 0:
        xrange = range(0, movex, 1)
    else:
        xrange = range(0, movex, -1)

    if movey > 0:
        yrange = range(0, movey, 1)
    else:
        yrange = range(0, movey, -1)
    print(f"movex = {movex}")
    print(f"movey = {movey}")

# Divide by zero is possible here. Need to fix
    if abs(movex) > abs(movey):
        slope = abs(movex) / abs(movey)
        for y in yrange:
            print(f"y is: {y}")
            if movey > 0 and movex > 0:
                cir.move(slope, 1)
            elif movey > 0 and movex < 0:
                cir.move(-slope, 1)
            elif movey < 0 and movex > 0:
                cir.move(slope, -1)
            else:
                cir.move(-slope, -1)
    else:
        slope = abs(movey) / abs(movex)
        for x in xrange:
            print(f"x is: {x}")
            if movex > 0 and movey > 0:
                cir.move(1, slope)
            elif movex > 0 and movey < 0:
                cir.move(1, -slope)
            elif movex < 0 and movey > 0:
                cir.move(-1, slope)
            else:
                cir.move(-1, -slope)
    print(f"schlope is {slope}")

#    for x in xrange:
#        print(f"x is: {x}")
#        if movex > 0:
#            cir.move(1, 0)
#        else:
#            cir.move(-1, 0)

#    for y in yrange:
#        print(f"y is: {y}")
#        if movey > 0:
#            cir.move(0, 1)
#        else:
#            cir.move(0, -1)
