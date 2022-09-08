import random
key=random.randint(1,100)
def game(life,guess):
    if(guess==key):
        print("You won!")
        return(0)
    elif(key>guess):
        if guess in range(key-5,key) :
            print("You are close ! Go high!")
        else:
            print("Go high!")
    else:
        if guess in range(key,key+5):
            print("You are close! Go Low!")
        else:
            print("Go Low!")
    return(life-1)
mode=input("Select level: easy or hard:\n").lower()
if(mode=="easy"):
    life=10
elif(mode=="hard"):
    life=5
else:
    print("Invalid command!")
while (life>0):
    choice=int(input("Guess a number\n"))
    c=game(life,choice)
    if(c==0):
        break
    print(f"No of  life remaining {c}")
    life=c
