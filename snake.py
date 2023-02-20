from turtle import Turtle

""" Constants for the Snake class """
START_POS = [(0, 0), (-10, 0), (-15, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
SNAKE_COLOR = ["#754c29"]
HEAD_SHAPE = ["circle", "square", "arrow", "triangle", "classic"]

""" initializing the class """


class Snake:
    def __init__(self):
        self.body = []
        self.start()
        self.head = self.body[0]
        self.move()
        self.last_pos = (self.body[-1].xcor(), self.body[-1].ycor())

    def snake_tail(self):
        # self.body[0].shapesize(stretch_len=1, stretch_wid=1)
        for part in self.body[1:]:
            part.shapesize(stretch_len=1, stretch_wid=1)
            part.shape("snake.gif")
        for part in self.body:
            if part == self.body[-2]:
                part.shapesize(stretch_len=1, stretch_wid=0.8)
                part.color("#754c29")
                part.shape("circle")
            if part == self.body[-1]:
                part.shapesize(stretch_len=1, stretch_wid=0.5)
                part.color("#754c29")
                part.shape("circle") 

    """ function to create the infant snake body(3 objects) """
    def start(self):
        for pos in START_POS:
            if pos == START_POS[0]:
                self.create(pos, "head0.gif")
            else:
                self.create(pos)
        self.snake_tail()

    """ function to create new body part """
    def create(self, position, shape="square"):
        new_body = Turtle(shape)
        new_body.penup()
        new_body.goto(position)
        new_body.color(SNAKE_COLOR[0])
        self.body.append(new_body)

    """ function to increase body count on snake """
    def grow(self):
        self.create(self.last_pos)
        self.snake_tail()

    """ function to remove dead snake and generate new snake """
    def new_snake(self):
        for part in self.body:
            part.goto(2000, -2000)
        self.body = []
        self.start()
        self.head = self.body[0]

    """ function to move entire snake """
    def move(self):
        for part in range(len(self.body) - 1, 0, -1):
            new_x = self.body[part - 1].xcor()
            new_y = self.body[part - 1].ycor()
            new_h = self.body[part - 1].heading()
            self.body[part].setheading(new_h)
            self.body[part].goto(new_x, new_y)    
        self.head.forward(DISTANCE)

    """ functions return X and Y coordinates of snakes head """
    def x_cor(self):
        return self.body[0].xcor()

    def y_cor(self):
        return self.body[0].ycor()

    """ function control snakes direction """
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.head.shape("head90.gif")

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.head.shape("head180.gif")

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.head.shape("head270.gif")

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.head.shape("head0.gif")