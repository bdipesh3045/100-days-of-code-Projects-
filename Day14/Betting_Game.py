 import random
whole=True
while whole:
    a=[11,1,2,3,4,5,6,7,8,9,10,10,10,10]
    a_total=0
    b_total=0
    play=[]
    deal=[]
    def player():
        global a_total
        data=random.randint(0,13)
        play.append(a[data])
        a_total+=a[data]
    def dealer():
        global b_total
        data=random.randint(0,13)
        deal.append(a[data])
        b_total+=a[data]
        if (len(deal)<2):
            print(f"Comp  scores:{deal} and total score is:  {b_total}")
    for x in range(0,2):
        player()
        dealer()
    print(f"You got the scores:{play} and your total score is: {a_total}")
    cont=True
    while cont:
        choice=input("Do you want to hit or stand: ")
        if (choice=="h"):
            player()
            dealer()
            print(f"You got the scores:{play} and your total score is: {a_total}")
        else:
            cont=False
    if (a_total>b_total and a_total<=21):
        print("You win!")
        print(f"You got the scores:{play} and your total score is: {a_total}")
        print(f"Comp  scores:{deal} and total score is:  {b_total}")
    elif (a_total<=21 and b_total>21):
        print("You win!")
        print(f"You got the scores:{play} and your total score is: {a_total}")
        print(f"Comp  scores:{deal} and total score is:  {b_total}")
    elif (a_total>21 and b_total>21):
        print("None of you won!")
        print(f"You got the scores:{play} and your total score is: {a_total}")
        print(f"Comp  scores:{deal} and total score is:  {b_total}")
    elif (a_total==b_total):
        print("Match drawn!")
        print(f"You got the scores:{play} and your total score is: {a_total}")
        print(f"Comp  scores:{deal} and total score is:  {b_total}")
    else:
        print("Computer win!!")
        print(f"You got the scores:{play} and your total score is: {a_total}")
        print(f"Comp  scores:{deal} and total score is:  {b_total}") 
    print("New Game\n")
    choose=input("Do you want to play again Y or N : ")
    if(choose=="N"):
        whole=False
print("Game finish")
