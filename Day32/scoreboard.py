from turtle import Turtle
sc=0
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,300)
        self.score=0
        self.write(f"Score:{self.score}",align="center", font=("Arial",24,"bold"))
        self.hideturtle()
        self.update()
    

    def update(self):
        self.write(f"Score:{self.score}",align="center", font=("Arial",24,"bold"))


    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score:{self.score}",align="center", font=("Arial",24,"bold"))


        