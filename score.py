from turtle import Turtle
FONT = ('Arial', 20, 'normal')
ALIGN = "center"
FONT_BIG = ("Times New Roman", 40, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.count = 0
        self.lvl = 0
        with open("data.txt", ) as data:
            self.content = int(data.read())
        self. high_score = self.content
        self.penup()
        self.color("green")
        self.goto(0, 270)
        self.hideturtle()
        self.speed(10)
        self.write_score()

    def new_score(self):
        self.count += 1
        if self.count > self.high_score:
            self.high_score = self.count
            with open("data.txt", mode="w") as data:
                data.write(f"{self.count}")
            print(self.count)
        self.write_score()

    def score_reset(self):
        self.count = 0
        self.lvl = 0
        self.write_score()

    def level_up(self):
        self.lvl += 1

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.count}        level: {self.lvl}           High Score: {self.high_score}",
                   font=FONT, align=ALIGN)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"   Score :{self.count}\nGame Over!!!", font=FONT_BIG, align=ALIGN)

