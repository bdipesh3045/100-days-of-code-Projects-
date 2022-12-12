from turtle import Turtle
import time
class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed('slow')
        self.color("white")
        
        self.penup()
        self.x_move=0.3
        self.y_move=0.3
        time.sleep(3)

        # self.goto(350,0)

    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)  
    
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
