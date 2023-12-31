from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor() < 250:
            self.forward(20)

    def down(self):
        if self.ycor() > -250:
            self.back(20)
