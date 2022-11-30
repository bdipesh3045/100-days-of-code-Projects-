from turtle import Screen
from scoreboard import Scoreboard
from snake_mod import Snake
from snake_food import Food
import time
screen =Screen()
screen.setup(width=500,height=500)
screen.bgcolor("Black")
screen.title("My snake game")
screen.tracer(0)

screen.bgpic("background.gif")


game_is_on = True
snake =Snake()
food=Food()
score= Scoreboard()
screen.listen()
screen.onkey(snake.w,"w")
screen.onkey(snake.s,"s")
screen.onkey(snake.d,"d")
screen.onkey(snake.a,"a")
screen.onkey(snake.space,"space")




while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    
    if snake.head.distance(food)< 12:
        food.refresh()
        snake.increase_length()
        score.increase_score()
        

    
  


screen.exitonclick()