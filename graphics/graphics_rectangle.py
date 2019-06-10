from graphics import *

def main():
    win = GraphWin("My Window", 900, 900)
    win.setBackground(color_rgb(0, 255, 255))

    rect = Rectangle(Point(200, 200), Point(700, 700))
    rect.setOutline(color_rgb(0, 0, 0))
    rect.setFill(color_rgb(255, 255, 0))
    rect.setWidth(10)
    rect.draw(win)

    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()
