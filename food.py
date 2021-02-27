from turtle import Turtle
import random


class Food(Turtle):
    '''this produces a black circle turtle first until you call another method'''
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.refresh_food()

    def refresh_food(self):
        xcor = random.randint(-270,270)
        ycor = random.randint(-270,270)
        self.goto(xcor, ycor)

    def hide_normal_food(self):
        self.goto(350,350)


def coordinate():
    xcor = random.randint(-270,280)
    ycor = random.randint(-270,280)
    return xcor, ycor


class BonusFoodOne(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.8)
        self.penup()
        self.color("blue")
        self.bonus_food1()

    def bonus_food1(self):
        coordinate()
        self.goto(coordinate())

    def hide_bonus_food1(self):
        self.goto(350,350)

    def show_bonus_food1_color(self):
        self.color("blue")

    def hide_bonus_food1_color(self):
        self.color("black")


class BonusFoodTwo(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1)
        self.penup()
        self.color("white")
        self.bonus_food2()

    def bonus_food2(self):
        coordinate()
        self.goto(coordinate())

    def hide_bonus_food2(self):
        self.goto(350,350)

    def show_bonus_food2_color(self):
        self.color("white")

    def hide_bonus_food2_color(self):
        self.color("black")

