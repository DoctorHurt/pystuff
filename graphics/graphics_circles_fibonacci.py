from graphics import *
import random

win = GraphWin("My Window", 800, 800)
win.setBackground(color_rgb(50, 50, 50))

# Function for nth Fibonacci number
def Fibonacci(n):
	if n<0:
		print("Incorrect input")
	# First Fibonacci number is 0
	elif n==1:
		return 0
	# Second Fibonacci number is 1
	elif n==2:
		return 1
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)

count = 1
while count < 20:
    fib = Fibonacci(count)
    pt = Point(fib, fib)
    cir = Circle(pt, 30)
    cir.setFill(color_rgb(255, 0, 0))
    cir.draw(win)
    count += 1

win.getMouse() # Pause to view result
win.close()    # Close window when done
