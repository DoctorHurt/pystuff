from graphics import *

def main():
    win = GraphWin("My Window", 500, 500)
    win.setBackground(color_rgb(100, 100, 0))
    
    ln = Line(Point(250, 250), Point(350, 450))
    ln.setOutline(color_rgb(0, 255, 255))
    ln.setWidth(5)
    ln.draw(win)
    
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()