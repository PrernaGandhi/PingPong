from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.right_player_score = 0
        self.left_player_score = 0
        self.update_scoreboard()

    def l_score(self):
        self.left_player_score += 1
        self.update_scoreboard()

    def r_score(self):
        self.right_player_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.display_score((-100, 200), self.left_player_score)
        self.display_score((100, 200), self.right_player_score)

    def display_score(self, position, player):
        self.goto(position)
        self.write(player, align=ALIGN, font=FONT)
