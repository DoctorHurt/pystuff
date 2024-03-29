""" Draw a circle, yo """

from graphics import *

def main():
    win = GraphWin("My Window", 500, 500)
    win.setBackground(color_rgb(100, 100, 0))

    pt = Point(250, 250)
    cir = Circle(pt, 50)
    cir.setFill(color_rgb(100, 244, 60))
    cir.draw(win)

    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()
