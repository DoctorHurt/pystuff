from graphics import *
from button import Button

win = GraphWin("My Robot Window", 1200, 800)
win.setBackground(color_rgb(100, 100, 100))

# Robot (its just a shape right now)
robot = Image(Point(400, 400), "bb8.png")
robot.draw(win)

# Lights
pwrLight = Circle(Point(280, 30), 20)
pwrLight.setFill(color_rgb(255, 0, 0))
pwrLight.draw(win)
engineLight = Circle(Point(480, 30), 20)
engineLight.setFill(color_rgb(255, 0, 0))
engineLight.draw(win)

# Buttons
pwrButton = Button(win, Point(200,30), 100, 30, "Power On/Off")
pwrButton.activate()
engineButton = Button(win, Point(380,30), 100, 30, "Motor On/Off")
engineButton.activate()
mvrtButton = Button(win, Point(650,65), 50, 30, "Right")
mvltButton = Button(win, Point(550,65), 50, 30, "Left")
mvupButton = Button(win, Point(600,30), 50, 30, "Up")
mvdnButton = Button(win, Point(600,100), 50, 30, "Down")
quitButton = Button(win, Point(50,30), 50, 30, "Quit")
quitButton.activate()

# Event loop
pt = win.getMouse()
pwrOn = False
engineOn = False
while not quitButton.clicked(pt):
    if pwrButton.clicked(pt) and pwrOn == False:
        pwrLight.setFill(color_rgb(0, 255, 0))
        pwrOn = True
    elif pwrButton.clicked(pt) and pwrOn == True:
        pwrLight.setFill(color_rgb(255, 0, 0))
        pwrOn = False
    elif engineButton.clicked(pt) and engineOn == False:
        engineLight.setFill(color_rgb(0, 255, 0))
        mvrtButton.activate()
        mvltButton.activate()
        mvupButton.activate()
        mvdnButton.activate()
        engineOn = True
    elif engineButton.clicked(pt) and engineOn == True:
        engineLight.setFill(color_rgb(255, 0, 0))
        mvrtButton.deactivate()
        mvltButton.deactivate()
        mvupButton.deactivate()
        mvdnButton.deactivate()
        engineOn = False
    elif mvrtButton.clicked(pt) and engineOn == True:
        robot.move(10,0)
    elif mvltButton.clicked(pt) and engineOn == True:
        robot.move(-10,0)
    elif mvdnButton.clicked(pt) and engineOn == True:
        robot.move(0,10)
    elif mvupButton.clicked(pt) and engineOn == True:
        robot.move(0,-10)
    pt = win.getMouse()

# close up shop
win.close()


# win.getMouse() # pause for click in window
# win.close() # Close window
