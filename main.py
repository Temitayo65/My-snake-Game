from turtle import Screen
import time
import random
from snake import Snake
from food import Food, BonusFoodOne, BonusFoodTwo
from scoreboard import ScoreBoard
from turtle import Turtle

my_screen = Screen()
my_screen.setup(height=600, width=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)

is_difficult = True
while is_difficult:
    # Type the difficulty you want for the game
    difficulty = my_screen.textinput("Difficulty level", "Which level do you want 'Easy' 'Medium' or 'Hard'").lower()
    if difficulty == "easy":
        sleep = 0.1
        wall = True
        is_difficult = False
    elif difficulty == "medium":
        sleep = 0.1
        wall = False
        is_difficult = False
    elif difficulty == "hard":
        sleep = 0.05
        wall = False
        is_difficult = False


def game():
    my_screen.clear()
    my_screen.bgcolor("black")
    my_screen.tracer(0)
    food = Food()
    snake = Snake()
    scoreboard = ScoreBoard()
    bonus_food1 = BonusFoodOne()
    bonus_food2 = BonusFoodTwo()
    bonus_food1.hide_bonus_food1()
    bonus_food2.hide_bonus_food2()

    snake.create_snake()
    my_screen.listen()
    my_screen.onkey(fun=snake.up, key="Up")
    my_screen.onkey(fun=snake.down, key="Down")
    my_screen.onkey(fun=snake.left, key="Left")
    my_screen.onkey(fun=snake.right, key="Right")

    blink = 1
    seconds_1 = 50
    seconds_2 = 30

    game_is_on = True
    while game_is_on:
        my_screen.update()
        time.sleep(sleep)
        snake.move()

        # Detects collision with food and give either another normal food or a bonus food
        if snake.my_turtle_list[0].distance(food) < 15:
            random_number = random.randint(1, 10)
            if random_number == 5:
                food.hide_normal_food()
                bonus_food2 = BonusFoodTwo()
                seconds_2 += -1
            elif random_number == 4 or random_number == 8:
                food.hide_normal_food()
                bonus_food1.bonus_food1()
                seconds_1 += -1
            else:
                food.refresh_food()
            snake.new_snake()
            scoreboard.write_score()

        #  Hides bonus_food1 after some seconds
        if 0 < seconds_1 < 50:
            seconds_1 += -1
        if seconds_1 == 0 and food.pos() == (350, 350):
            bonus_food1.hide_bonus_food1()
            food.refresh_food()
            seconds_1 = 50

        # Hides bonus_food2 after some seconds
        if 0 < seconds_2 < 30:
            seconds_2 -= 1
        if seconds_2 == 0 and food.pos() == (350, 350):
            bonus_food2.hide_bonus_food2()
            food.refresh_food()
            seconds_2 = 30

        # Detects collision between the snake and the bonus food
        if snake.my_turtle_list[0].distance(bonus_food1) < 25:
            bonus_food1.hide_bonus_food1()
            scoreboard.bonus_score1()
            seconds_1 = 50
            food = Food()
        if snake.my_turtle_list[0].distance(bonus_food2) < 25:
            bonus_food2.hide_bonus_food2()
            scoreboard.bonus_score2()
            seconds_2 = 30
            food = Food()

        # Detects collision with self
        for item in snake.my_turtle_list[1:]:
            if snake.my_turtle_list[0].distance(item) < 10:
                scoreboard.game_over()
                game_is_on = False

        # Detects collision with wall
        if wall:
            snake.position_snake()
        else:
            if snake.my_turtle_list[0].xcor() > 290 or snake.my_turtle_list[0].xcor() < -290 \
                    or snake.my_turtle_list[0].ycor() > 290 or snake.my_turtle_list[0].ycor() < -290:
                scoreboard.game_over()
                game_is_on = False

        # Detects collision with self
        for item in snake.my_turtle_list[1:]:
            if snake.my_turtle_list[0].distance(item) < 10:
                scoreboard.game_over()
                game_is_on = False

        # blinks bonus food
        if blink % 2 == 0:
            bonus_food1.show_bonus_food1_color()
            bonus_food2.show_bonus_food2_color()
            blink += 1
        else:
            bonus_food1.hide_bonus_food1_color()
            bonus_food2.hide_bonus_food2_color()
            blink += 1

        #   Restarts game
        if scoreboard.pos() == (0, 0):
            my_screen.clear()
            my_screen.bgcolor("black")
            playing_turtle = Turtle()
            playing_turtle.penup()
            playing_turtle.hideturtle()
            playing_turtle.color("white")
            scoreboard.above_game_over()
            scoreboard.position_score()
            playing_turtle.write("Press enter to start again", False, "center", ("courier", 12, "bold"))
            my_screen.onkey(game, "Return")
    my_screen.exitonclick()


game()
