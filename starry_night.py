

from turtle import *        # importing everything from turtle library
from random import *        # importing everything from random library

speed(0)                    # to increase the speed

bgcolor("black")            # setting background color black 
hideturtle()                # to hide the black turtle tip

width = window_width()      # getting width of window
height = window_height()    # getting height of window

# setting function to create star 
def create_star(x, y):
    size = randrange(2,15)  # using random range to pick random number between 2 to 20.
    penup()                 # lifting the tip before drawing
    goto(x,y)               # it moves star to the x & y position
    pendown()               # putting the pendown to draw
    dot(size, "white")      # to draw a circle with a given diameter(size) and white color

# to generate lots of stars, we are going to use for loop to repeat the above algorithm
for x in range(100):
    x = randrange(-width/2, width/2) # creating x position variable with x & -x axis side for stars
    y = randrange(-height/2, height/2)# creating y position vaiable with y & -y axis side for stars  
    create_star(x, y)       # calling function inside loop with new x,y coordinates. 


done()  # to stop te code and show the window



