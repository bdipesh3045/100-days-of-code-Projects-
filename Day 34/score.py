from turtle import Turtle
sc=0
class Scoreboard(Turtle):
    
    def __init__(self,name,var):
        super().__init__()
        self.penup()
        if var=="r":
            self.goto(470,0)
        else:
            self.goto(-460,0)
        self.color("white")
        self.score=0
        self.name=name
        self.hideturtle()
        self.update()
    

    def update(self):
        self.write(f"Player {self.name}\n Score:{self.score}",align="center", font=("Arial",24,"bold"))


    def increase_score(self):
        self.score+=1
        self.clear()
        self.update()
        # self.write(f"Score:{self.score}",align="center", font=("Arial",24,"bold"))