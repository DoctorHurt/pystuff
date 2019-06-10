from graphics import *

def main():
    win = GraphWin("My Window", 800, 800)
    win.setBackground(color_rgb(0, 255, 255))
    
    cir = Circle(Point(400, 400), 300)
    cir.setOutline(color_rgb(0, 0, 0))
    cir.setFill(color_rgb(255, 255, 0))
    cir.setWidth(10)
    cir.draw(win)
    
    eye1 = Circle(Point(300, 300), 50)
    eye1.setOutline(color_rgb(0, 0, 0))
    eye1.setFill(color_rgb(0, 0, 255))
    eye1.setWidth(3)
    eye1.draw(win)

    eye2 = Circle(Point(500, 300), 50)
    eye2.setOutline(color_rgb(0, 0, 0))
    eye2.setFill(color_rgb(0, 0, 255))
    eye2.setWidth(3)
    eye2.draw(win)

    nose = Circle(Point(400, 390), 35)
    nose.setOutline(color_rgb(0, 0, 0))
    nose.setFill(color_rgb(0, 255, 0))
    nose.setWidth(3)
    nose.draw(win)

    mouth = Polygon(Point(300, 500),
                    Point(400, 600),
                    Point(500, 500))
    mouth.setOutline(color_rgb(0, 0, 0))
    mouth.setFill(color_rgb(255, 0, 0))
    mouth.setWidth(3)
    mouth.draw(win)

    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()