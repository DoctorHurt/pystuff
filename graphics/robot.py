from graphics import *
from button import Button

win = GraphWin("My Robot Window", 1200, 800)
win.setBackground(color_rgb(100, 100, 100))

# Robot
robot = Image(Point(400, 400), "bb8.png")
robot.draw(win)

# Stormtrooper
stormtrooper = Image(Point(600, 400), "stormtrooper.png")
stormtrooper.draw(win)

# Lights
pwrLight = Circle(Point(280, 30), 20)
pwrLight.setFill(color_rgb(255, 0, 0))
pwrLight.draw(win)
motorLight = Circle(Point(480, 30), 20)
motorLight.setFill(color_rgb(255, 0, 0))
motorLight.draw(win)

# Buttons
pwrButton = Button(win, Point(200,30), 100, 30, "Power On/Off")
pwrButton.activate()
motorButton = Button(win, Point(380,30), 100, 30, "Motor On/Off")
mvrtButton = Button(win, Point(650,65), 50, 30, "Right")
mvltButton = Button(win, Point(550,65), 50, 30, "Left")
mvupButton = Button(win, Point(600,30), 50, 30, "Up")
mvdnButton = Button(win, Point(600,100), 50, 30, "Down")
quitButton = Button(win, Point(50,30), 50, 30, "Quit")
quitButton.activate()

# Event loop
pt = win.getMouse()
pwrOn = False
motorOn = False
while not quitButton.clicked(pt):
    if pwrButton.clicked(pt) and pwrOn == False:
        pwrLight.setFill(color_rgb(0, 255, 0))
        pwrOn = True
        motorButton.activate()
        where = robot.getAnchor()
        robotOn = Image(where, "bb8-on.png")
        robotOn.draw(win)
        robot.undraw()
    elif pwrButton.clicked(pt) and pwrOn == True:
        pwrLight.setFill(color_rgb(255, 0, 0))
        pwrOn = False
        motorButton.deactivate()
        motorLight.setFill(color_rgb(255, 0, 0))
        mvrtButton.deactivate()
        mvltButton.deactivate()
        mvupButton.deactivate()
        mvdnButton.deactivate()
        motorOn = False
        where = robotOn.getAnchor()
        robot = Image(where, "bb8.png")
        robot.draw(win)
        robotOn.undraw()
    elif motorButton.clicked(pt) and motorOn == False:
        motorLight.setFill(color_rgb(0, 255, 0))
        mvrtButton.activate()
        mvltButton.activate()
        mvupButton.activate()
        mvdnButton.activate()
        motorOn = True
    elif motorButton.clicked(pt) and motorOn == True:
        motorLight.setFill(color_rgb(255, 0, 0))
        mvrtButton.deactivate()
        mvltButton.deactivate()
        mvupButton.deactivate()
        mvdnButton.deactivate()
        motorOn = False
    elif mvrtButton.clicked(pt) and motorOn == True:
        robotOn.move(10,0)
    elif mvltButton.clicked(pt) and motorOn == True:
        robotOn.move(-10,0)
    elif mvdnButton.clicked(pt) and motorOn == True:
        robotOn.move(0,10)
    elif mvupButton.clicked(pt) and motorOn == True:
        robotOn.move(0,-10)
    pt = win.getMouse()

# close up shop
win.close()


# win.getMouse() # pause for click in window
# win.close() # Close window
