from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, positions, width, len):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=width, stretch_len=len)
        self.speed("fastest")
        self.goto(positions)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
