import random
li=[]
sped=["fastest","fast","normal","slow","slowest"]
def spd():
    ot=True
    while ot:
        print("in")
        k=random.choice(sped)
        if k not in li:
            a=False
    li.append(k)
    return(k)
print(spd())