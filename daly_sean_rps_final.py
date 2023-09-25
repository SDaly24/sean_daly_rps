# This file was created by: Sean Daly

'''
Goals:
When a user click on rock, paper, or scissors, the computer randomly chooses their choice and displays the result
Code is displayed in a graphic rather than the terminal 
'''

# imports the turtle module which creates a graphic interface for the user
import turtle
from turtle import *
# The os module allows us to access the current directory in order to access assets
import os
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

# Here, we define the sleep function as a value of time.Therefore, sleep(1) will makes the code sleep for one second
from time import sleep

# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')

# setup the width and height for the window of the turtule module
WIDTH, HEIGHT = 1000, 400

# setup the width and height of the rock, paper, and scissors images
rock_w, rock_h = 256, 280

paper_w, paper_h = 256, 204

scissors_w, scissors_h = 256, 170


# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")


# canvas object
cv = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)


# setup the rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')
# instantiate (create an instance of) the Turtle class for the rock
rock_instance = turtle.Turtle()
# setup the paper image using the os module as paper_image
paper_image = os.path.join(images_folder, 'paper.gif')
# instantiate (create an instance of) the Turtle class for the paper
paper_instance = turtle.Turtle()
# setup the scissors image using the os module as scissors_image
scissors_image = os.path.join(images_folder, 'scissors.gif')
# instantiate (create an instance of) the Turtle class for the scissors
scissors_instance = turtle.Turtle()

# Rather than showing rock in the terminal as text, the function "show_rock" makes the rock appear in the turle instead as a graphic
def show_rock(x,y):
    # add the rock image as a shape
    screen.addshape(rock_image)
    # attach the rock_image to the rock_instance
    rock_instance.shape(rock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    rock_instance.penup()
    # set the position of the rock_instance
    rock_instance.setpos(x,y)

# Rather than showing paper in the terminal as text, the function "show_paper" makes the paper appear in the turle instead as a graphic
def show_paper(x,y):
    # add the paper image as a shape
    screen.addshape(paper_image)
    # attach the paper_image to the paper_instance
    paper_instance.shape(paper_image)
    # remove the pen option from the paper_instance so it doesn't draw lines when moved
    paper_instance.penup()
    # set the position of the paper_instance
    paper_instance.setpos(x,y)
        
# Rather than showing scissors in the terminal as text, the function "show_scissors" makes the scissors appear in the turle instead as a graphic
def show_scissors(x,y):
    # add the scissors image as a shape
    screen.addshape(scissors_image)
    # attach the scissors_image to the scissors_instance
    scissors_instance.shape(scissors_image)
    # remove the pen option from the scissors_instance so it doesn't draw lines when moved
    scissors_instance.penup()
    # set the position of the scissors_instance
    scissors_instance.setpos(x,y)

# instantiate a generic turtle
t = turtle.Turtle()
# instantiate a turtle for writing text
text = turtle.Turtle()
text.color('deep pink')
text.hideturtle()

# hide that turtle
t.hideturtle()

# This sets up the coordinates for the rock, paper, and scissors images in the turtle graphic
show_rock(-300, 0)
show_paper(0,0)
show_scissors(300,0)

# this function uses and x y value, an obj, and width and height
# it checks whether the mouse collides with the following x, y, width and height 
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] - w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False

# function that passes through wn onlick
# This defines the position of the text and writes "Choose rock, paper, or scissors" in turtle
text.setpos(0,150)
text.write("Choose rock, paper or scissors", False, "left", ("Arial", 24, "normal"))


'''
This imports a random integer from (0,2)
It assigns string values to each random ineteger that can be picked
It also defines these values under the cpu_select function
''' 
from random import randint
def cpu_select():
    choices = ["rock", "paper", "scissors"]
    return choices[randint(0,2)]

'''
the def mouse_pos defines that our mouse position is measured in x and y values
the collide function checks if the mouse_pos is between the (x,y, the instance, the width and the height)
if the mouse position is between anyone of these coordinates, it will print that the "player chose rock" and then define the outcome of the game based on what random string value the cpu chose
if the mouse position isn't on an icon, it prints "you chose nothing"
'''
def mouse_pos(x, y):
    
    if collide(x,y,rock_instance, rock_w, rock_h):
        cpu_picked = cpu_select()
        print("rock")
        text.setpos(-400,-175)
        text.write("Player chose rock", False, "left", ("Arial", 24, "normal"))
        sleep(0.5)
        # need computer to randomly choose
        # need to display what the computer and and communicate winner
        
        
        # This defines the outcome if player picks rock and cpu picks rock.
        if cpu_picked== "rock":
           # This clears the text from above "Choose rock, paper, or scissors"
           text.clear()
           # This hides the images that aren't selected by the player or cpu.
           scissors_instance.hideturtle()
           paper_instance.hideturtle() 
           # The following lines define where the text is written, and what the outcome of the game is.
           text.penup()
           text.setpos(-400,175)
           text.write("CPU chose: rock... It's a Tie!", False, "left", ("Arial", 24, "normal"))
        # This defines the outcome if player picks rock and cpu picks paper.
        if cpu_picked == "paper":
            # This clears the text from above "Choose rock, paper, or scissors"
            text.clear()
            # This hides the images that aren't selected by the player or cpu.
            scissors_instance.hideturtle()
            # The following lines define where the text is written, and what the outcome of the game is.
            text.penup() 
            text.setpos(-400,175)
            text.write("CPU chose: paper... The computer won:(", False, "left", ("Arial", 24, "normal"))
        # This defines the outcome if player picks rock and cpu picks scissors.
        if cpu_picked == "scissors":
            # This clears the text from above "Choose rock, paper, or scissors"
            text.clear()
            # This hides the images that aren't selected by the player or cpu.
            paper_instance.hideturtle()
            # The following lines define where the text is written, and what the outcome of the game is.
            text.penup()
            text.setpos(-400,175)
            text.write("CPU chose: scissors... You win!", False, "left", ("Arial", 24, "normal"))
# This has the same logic and process that is explained from line 134-137, but its used to check if paper is selected.
    elif collide(x,y,paper_instance, paper_w, paper_h):
        cpu_picked = cpu_select()
        print("paper")
        text.setpos(-100,-150)
        text.write("Player chose paper", False, "left", ("Arial", 24, "normal"))
        sleep(0.5)
        # This defines the outcome if player picks paper and cpu picks rock.
        if cpu_picked== "rock":
           # This clears the text from above "Choose rock, paper, or scissors"
           text.clear()
           # This hides the images that aren't selected by the player or cpu.
           scissors_instance.hideturtle()
           # The following lines define where the text is written, and what the outcome of the game is.
           text.penup()
           text.setpos(-400,175)
           text.write("CPU chose: rock... You won!", False, "left", ("Arial", 24, "normal"))
         # This defines the outcome if player picks paper and cpu picks paper.
        if cpu_picked == "paper":
            # This clears the text from above "Choose rock, paper, or scissors"
            text.clear()
            # This hides the images that aren't selected by the player or cpu.
            scissors_instance.hideturtle()
            rock_instance.hideturtle()
            # The following lines define where the text is written, and what the outcome of the game is.
            text.penup() 
            text.setpos(-400,175)
            text.write("CPU chose: paper... It's a tie!", False, "left", ("Arial", 24, "normal"))
         # This defines the outcome if player picks paper and cpu picks scissors.
        if cpu_picked == "scissors":
            # This clears the text from above "Choose rock, paper, or scissors"
            text.clear()
            # This hides the images that aren't selected by the player or cpu.
            rock_instance.hideturtle()
            # The following lines define where the text is written, and what the outcome of the game is.
            text.penup()
            text.setpos(-400,175)
            text.write("CPU chose: scissors... You lost :(", False, "left", ("Arial", 24, "normal"))
 # This has the same logic and process that is explained from line 134-137, but its used to check if scissor is selected.   
    elif collide(x,y,scissors_instance, scissors_w, scissors_h):
        cpu_picked = cpu_select()
        print("scissors")
        text.setpos(190,-150)
        text.write("Player chose scissors", False, "left", ("Arial", 24, "normal"))
        sleep(0.5)
        # This defines the outcome if player picks scissors and cpu picks rock.
        if cpu_picked == "rock":
           # This clears the text from above "Choose rock, paper, or scissors"
           text.clear()
           # This hides the images that aren't selected by the player or cpu.
           paper_instance.hideturtle()
           text.penup()
           text.setpos(-400,170)
           text.write("CPU chose: rock... You lost :(", False, "left", ("Arial", 24, "normal"))
        # This defines the outcome if player picks scissors and cpu picks paper.
        if cpu_picked == "paper":
            # This clears the text from above "Choose rock, paper, or scissors"
            text.clear()
            # This hides the images that aren't selected by the player or cpu.
            rock_instance.hideturtle()
            text.penup() 
            text.setpos(-400,170)
            text.write("CPU chose: paper... You won!!", False, "left", ("Arial", 24, "normal"))
        # This defines the outcome if player picks scissors and cpu picks scissors.
        if cpu_picked == "scissors":
            # This clears the text from above "Choose rock, paper, or scissors"
            text.clear()
            # This hides the images that aren't selected by the player or cpu.
            rock_instance.hideturtle()
            paper_instance.hideturtle()
            text.penup()
            text.setpos(-400,170)
            text.write("CPU chose: scissors... It's a tie", False, "left", ("Arial", 24, "normal"))
    else: 
        print("you chose nothing")
        text.setpos(-150,-200)
        text.write("you chose nothing", False, "left", ("Arial", 24, "normal"))



# user this to get mouse position
screen.onclick(mouse_pos)
# runs mainloop for Turtle - required to be last
screen.mainloop()