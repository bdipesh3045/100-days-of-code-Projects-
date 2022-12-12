from turtle import Screen
from paddle import Paddle
from pong import Pong
from score import Scoreboard
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("Black")
screen.title("Ping Pong Game")
screen.tracer(0)
pong=Pong()

score_r=Scoreboard("Dipesh","r")
score_l=Scoreboard("XYZ","l")

r_paddle=Paddle(350,0)
l_paddle=Paddle(-350,0)
screen.listen()
screen.onkey(l_paddle.w,"w")
screen.onkey(l_paddle.s,"s")

screen.onkey(r_paddle.w,"p")
screen.onkey(r_paddle.s,"l")


Game=True
while Game:
    screen.update()
    pong.move()
    if pong.ycor()>350 or pong.ycor()< -350:
        pong.bounce_y()


    if  pong.distance(r_paddle)< 26 and pong.xcor()> 340:
        pong.bounce_x()
        score_r.increase_score()

    if pong.xcor()<-365 or pong.xcor()>365:
        pong.bounce_x()



    if pong.distance(l_paddle)< 30 and pong.xcor()< -340:
        pong.bounce_x()
        score_l.increase_score()

    
 


    

# screen.onkey(paddle.p,"p")
# screen.onkey(paddle.l,"l")
 



screen.exitonclick()