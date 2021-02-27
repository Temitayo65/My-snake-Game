from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.x_axis = 0
        self.my_turtle_list = []

    def create_snake(self):
        for i in range(3):
            my_turtle = Turtle()
            my_turtle.penup()
            my_turtle.goto(x=self.x_axis, y=0)
            my_turtle.shape("square")
            my_turtle.color("white")
            self.x_axis += -20
            self.my_turtle_list.append(my_turtle)

    def new_snake(self):
        list_length = len(self.my_turtle_list)-1
        last_x_axis = self.my_turtle_list[list_length].xcor()
        last_y_axis = self.my_turtle_list[list_length].ycor()
        my_turtle = Turtle("square")
        my_turtle.color("white")
        my_turtle.penup()
        self.my_turtle_list.append(my_turtle)
        my_turtle.goto(last_x_axis, last_y_axis)

    def move(self):
        for items in range(len(self.my_turtle_list)-1, 0, -1):
            xcor = self.my_turtle_list[items - 1].xcor()
            ycor = self.my_turtle_list[items - 1].ycor()
            self.my_turtle_list[items].goto(xcor, ycor)
        self.my_turtle_list[0].forward(MOVE_DISTANCE)

    def position_snake(self):
        if self.my_turtle_list[0].xcor() > 290:
            current_y = self.my_turtle_list[0].ycor()
            self.my_turtle_list[0].goto(-290, current_y)
        if self.my_turtle_list[0].xcor() < -290:
            current_y = self.my_turtle_list[0].ycor()
            self.my_turtle_list[0].goto(290, current_y)
        if self.my_turtle_list[0].ycor() > 290:
            current_x = self.my_turtle_list[0].xcor()
            self.my_turtle_list[0].goto(current_x, -290)
        if self.my_turtle_list[0].ycor() < -290:
            current_x = self.my_turtle_list[0].xcor()
            self.my_turtle_list[0].goto(current_x, 290)

    def up(self):
        if self.my_turtle_list[0].heading() != 270:
            self.my_turtle_list[0].setheading(90)

    def down(self):
        if self.my_turtle_list[0].heading() != 90:
            self.my_turtle_list[0].setheading(270)

    def left(self):
        if self.my_turtle_list[0].heading() != 0:
            self.my_turtle_list[0].setheading(180)

    def right(self):
        if self.my_turtle_list[0].heading() != 180:
            self.my_turtle_list[0].setheading(0)
