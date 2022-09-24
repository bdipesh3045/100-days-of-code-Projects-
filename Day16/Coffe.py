resources={
    "water": 1000,
    "coffe":850,
    "milk":600,
    "price":0
}
latte={
    "water":30,
    "coffe":20,
    "milk":10,
    "price":15
}
expresso={
    "water":200,
    "coffe":10,
    "milk":15,
    "price":30
}
capuccino={
    "water":20,
    "coffe":10,
    "milk":25,
    "price":25
}
def check():
    global drink_coffe
    score=0
    data=""
    for i in resources:
        if (resources[i]>=choice[i]) and i!="price":
            score+=1
        else:
            if i!="price":
                data=i
    if (score>=3):
        print("Your coffe is being made:")
        bool=True
    else:
        print(f"Ensufficient resource. Please refill {data}\n Choose another type of coffee!")
        bool=False
        drink_coffe=False
    if bool==True:
        for i in resources:
            if not i=="price":
                resources[i]=resources[i]-choice[i]
            else:
                resources[i]=resources[i]+choice[i]
    print("The remaining Resouces:")
    for i in resources:
        print(f"{i}:{resources[i]}")
drink_coffe=True
while drink_coffe:
    choice=""
    b=False
    while not b:
        a=int(input("NO of favour avaliable:\nChoose between the three option avaliable:\n1.latte\n2.expresso\n3.capuccino\n>"))
        b=True
        if (a==1):
            choice=latte
        elif(a==2):
            choice=expresso
        elif(a==3):
            choice=capuccino
        else:
            b=False
    check()
    more=input("Do you want to drnk more coffe (y or n)")
    if(more=="n"):
        drink_coffe=False

    
    
        
    
        
            


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
