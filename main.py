from turtle import Turtle, Screen
#import time
from time import sleep
from Snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screnn.setup(width=600, height=600)
screen.bgcolor("AliceBlue")
screen.title("My Snake game")

starting_position = [(0,0), (-20,0), (-40,0)]
serpent = Snake()
food = Food()
scoreboard = Scoreboard()
game_is_on = True
Sleep_speed = 0,1
screen.onkey(serpent.up, "Up")
screen.onkey(serpent.down, "Down")
screen.onkey(serpent.left, "Left")
screen.onkey(serpent.right, "Right")

while game_is_on:
    screen.update()
    sleep(Sleep_speed)
    serpent.move()
    #detect collision wiht food
    if serpent.segments[0].distance(food)  < 15:
        food.refresh()
        serpent.extend()
        scoreboard.increase_score()
    #detect collision wiht wall
    if serpent.segments[0].xcor() > 280 or serpent.segments[0].xcor() < -280 or serpent.segments[0].ycor()  >280 or serpent.segments[0].ycor()  < -280:       
        game_is_on = False
        scoreboard.game_over()
        scoreboard.reset()
        sleep(5)
        screen.bye()


screen.exitonclick()