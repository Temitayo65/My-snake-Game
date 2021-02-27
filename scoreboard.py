from turtle import Turtle
FONT_TYPE = "courier"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.score = 0
        self.position_score()

    def position_score(self):
        self.goto(0,280)
        self.write(f"score = {self.score}", False, "center", (FONT_TYPE, 12, "bold"))

    def above_game_over(self):
        self.goto(0,30)
        self.color("white")
        self.write("GAME OVER", False, "center", (FONT_TYPE, 12, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write("GAME OVER", False, "center", (FONT_TYPE, 12, "bold"))

    def write_score(self):
        self.clear()
        self.score += 1
        self.write(f"score = {self.score}",False,"center",(FONT_TYPE,12,"bold"))

    def bonus_score1(self):
        self.clear()
        self.score += 3
        self.write(f"score = {self.score}", False, "center", (FONT_TYPE, 12, "bold"))

    def bonus_score2(self):
        self.clear()
        self.score += 5
        self.write(f"score = {self.score}", False, "center", (FONT_TYPE, 12, "bold"))


