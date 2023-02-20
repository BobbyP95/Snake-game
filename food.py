from turtle import Turtle,Screen
from random import randrange

screen = Screen()




class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('rat2.gif')
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.color("green")
        self.penup()
        self.speed(10)
        self.goto(200, 0)
        
    def respawn(self):
        random_x = randrange(260, -260, -20)
        random_y = randrange(250, -260, -20)
        self.goto(random_x, random_y)
