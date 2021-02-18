from turtle import Turtle

FONT_ALIGNMENT = "Courier"
FONT_SIZE = 60
L_SCOREBOARD_X_POSITION = -100
L_SCOREBOARD_Y_POSITION = 200
R_SCOREBOARD_X_POSITION = 100
R_SCOREBOARD_Y_POSITION = 200


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.l_score= 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(L_SCOREBOARD_X_POSITION, L_SCOREBOARD_Y_POSITION)
        self.write(self.l_score, align="center", font=(FONT_ALIGNMENT, FONT_SIZE, "normal"))
        self.goto(R_SCOREBOARD_X_POSITION, R_SCOREBOARD_Y_POSITION)
        self.write(self.r_score, align="center", font=(FONT_ALIGNMENT, FONT_SIZE, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
