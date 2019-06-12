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
engineButton = Button(win, Point(380,30), 100, 30, "Engine On/Off")
engineButton.activate()
mvrtButton = Button(win, Point(300,100), 100, 30, "Move Right")
mvrtButton.activate()
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
        engineOn = True
    elif engineButton.clicked(pt) and engineOn == True:
        engineLight.setFill(color_rgb(255, 0, 0))
        engineOn = False
    elif mvrtButton.clicked(pt) and engineOn == True:
        robot.move(10,0)

    pt = win.getMouse()

# close up shop
win.close()


# win.getMouse() # pause for click in window
# win.close() # Close window
