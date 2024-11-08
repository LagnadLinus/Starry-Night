

from turtle import *        # importing everything from turtle library
from random import *        # importing everything from random library

speed(0.5)                    # to increase the speed

bgcolor("midnight blue")    # setting background color midnight blue to give dusk/dawn effect
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

# function to create moon
def create_moon():
    penup()                 # making penup first 
    goto(width/4, height/4) # adding the moon in the upper right corner
    pendown()               # Starts drawing
    color("light yellow")   # selecting color
    begin_fill()            # adding color
    circle(50)              # making circle of size 50px
    end_fill()              # stopping fill

# function to generate lots of stars, we are going to use for loop to repeat the above algorithm
for x in range(200):
    x = randrange(-width/2, width/2) # creating x position variable with x & -x axis side for stars
    y = randrange(-height/2, height/2)# creating y position vaiable with y & -y axis side for stars  
    create_star(x, y)       # calling function inside loop with new x,y coordinates. 

create_moon() #draws the moon

done()  # to stop te code and show the window output



