from turtle import Turtle

import time

up=90
down=270
left=180
right=0

starting_position=[(0,0),(-20,0),(-40,0)]

cont_snake=10

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head= self.segments[0]

    def create_snake(self):
        for position in starting_position:
            new_segment =Turtle("square")
            new_segment.color("brown")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    
    def increase_length(self):
            new_segment =Turtle("square")
            new_segment.color("brown")
            new_segment.penup()
            self.segments.append(new_segment)

    def move_snake(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            seg_x = self.segments[seg_num-1].xcor()
            seg_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(seg_x,seg_y)
        self.head.forward(cont_snake)
    
    def w(self):
        if self.head.heading() !=down:
            self.head.setheading(up)
    
    def s(self):
        if self.head.heading() !=up:
            self.head.setheading(down)
    
    def d(self):
        if self.head.heading() !=left:
            self.head.setheading(right)
    
    def a(self):
        if self.head.heading() !=right:
            self.head.setheading(left)
    
    def space(self):
        time.sleep(5)
    
    
    
    
