from graphics import *

def main():
    win = GraphWin("My Window", 800, 900)
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

    eyeball1 = Circle(Point(300, 300), 20)
    eyeball1.setOutline(color_rgb(0, 0, 0))
    eyeball1.setFill(color_rgb(255, 0, 0))
    eyeball1.setWidth(3)
    eyeball1.draw(win)

    eye2 = Circle(Point(500, 300), 50)
    eye2.setOutline(color_rgb(0, 0, 0))
    eye2.setFill(color_rgb(0, 0, 255))
    eye2.setWidth(3)
    eye2.draw(win)

    eyeball2 = Circle(Point(500, 300), 20)
    eyeball2.setOutline(color_rgb(0, 0, 0))
    eyeball2.setFill(color_rgb(255, 0, 0))
    eyeball2.setWidth(3)
    eyeball2.draw(win)

    nose = Circle(Point(400, 390), 35)
    nose.setOutline(color_rgb(0, 0, 0))
    nose.setFill(color_rgb(0, 255, 0))
    nose.setWidth(3)
    nose.draw(win)

    mouth = Polygon(Point(300, 500),
                    Point(400, 600),
                    Point(500, 500),
                    Point(400, 550))
    mouth.setOutline(color_rgb(0, 0, 0))
    mouth.setFill(color_rgb(255, 0, 0))
    mouth.setWidth(3)
    mouth.draw(win)

    hair1 = Line(Point(400, 100), Point(400, 50))
    hair1.setWidth(3)
    hair1.draw(win)

    hair2 = Line(Point(410, 100), Point(410, 50))
    hair2.setWidth(3)
    hair2.draw(win)

    hair3 = Line(Point(390, 100), Point(390, 50))
    hair3.setWidth(3)
    hair3.draw(win)

    hair4 = Line(Point(380, 100), Point(380, 50))
    hair4.setWidth(3)
    hair4.draw(win)

    hair5 = Line(Point(420, 100), Point(420, 50))
    hair5.setWidth(3)
    hair5.draw(win)

    img = Image(Point(400, 770), r"C:\Users\jeremyp\Documents\Pystuff\bodysmall.gif")
    img.draw(win)

    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()
