import const
import random
from datetime import datetime


x=[0,0,0]

def countKing(cards):
    n=0
    for i in cards:
        if i>const.MAX_CARD_NUM-4:
            n=n+1
    return n

def countKing2(cards,king):
    n=0
    for i in cards:
        if i>king and i<=king+4:
            n=n+1
    return n

ms=datetime.now().microsecond
random.seed(ms)
cards1=[]
cards2=[]

cards=[i for i in range(1, const.MAX_CARD_NUM+1)]

print("Try %d times, %d cards" % (const.MAX_TRY, const.MAX_CARD_NUM))
print("Try \t 0:4 \t 1:3 \t 2:2")
for i in range(1,const.MAX_TRY+1):
    cards1.clear()
    cards2.clear()
    for j in range(0, const.MAX_CARD_NUM):
        if random.random()> 0.5:
            cards1.append(cards[j])
        else:
            cards2.append(cards[j])  

    while len(cards1)>len(cards2):
        cards2.append(cards1[1])
        cards1.remove(cards1[1])

    while len(cards2)>len(cards1):
        cards1.append(cards2[1])
        cards2.remove(cards2[1])
    
    king1=countKing(cards1)
    king2=countKing(cards2)

    cards=cards1+cards2

    if (king1==0 and king2==4) or (king1==4 and king2==0):
        x[0]=x[0]+1
    else:
        if (king1==1 and king2==3) or (king1==3 and king2==1):
            x[1]=x[1]+1
        else:
            if king1==2 and king2==2:
                x[2]=x[2]+1
            else:
                print("ERROR", king1, king2)

    if (i % 10000 ==0):
        print("%d \t %5.1f \t %5.1f \t %5.1f" % (i, x[0]*100./i ,x[1]*100./i, x[2]*100./i ))



