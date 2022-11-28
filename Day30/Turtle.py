import turtle as turtle_module
import random
import time
turtle_module.colormode(255)
x_cor=30
y_cor=30
z=2
opp=""
bet=input("Bet among 5 turtle:")
time.sleep(5)

li=[]

def spd():
    ot=True
    while ot:
        k=random.choice(["fastest","fast","normal","slow","slowest"])
        if k not in li:
            ot=False
    ot=True
    li.append(k)
    return(k)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    my_tuple=(r,g,b)
    return(my_tuple)
all=True

for i in range(1,6):
    a=f"tim{i}"
    a=turtle_module.Turtle()
    if(i!=1):
        if (z%2==0):
            a.setheading(90)
            a.forward(x_cor)
            x_cor+=30
        else:
            a.setheading(270)
            a.forward(y_cor)
            y_cor+=30
    a.color(random_color())
    z+=1
    a.shape("turtle")
    a.setheading(180)
    a.forward(600)
    dat=spd()
    a.setheading(0)
    if(dat=="fastest"):
        opp=i
    a.speed(dat)
    
    a.forward(1200)   
        
if(int(bet)==int(opp)):
    print("You won:")
else:
    print("You Loose!")
    




screen=turtle_module.Screen()


screen.exitonclick()


