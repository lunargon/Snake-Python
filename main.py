import time
from snake import Snake
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=480, height=360)  # 360p Screen
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.11)
    snake.move()

screen.exitonclick()
