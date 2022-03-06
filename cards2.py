import const
import random
from datetime import datetime


x=[0,0,0]

class card:
    x=0.0
    num=0
    def __init__(self, x, num):
        self.x=x
        self.num=num

def countKing(cards):
    k1=0
    k2=0
    for i in range(0, const.MAX_CARD_NUM):        
        if cards[i].num>const.MAX_CARD_NUM-4:
            if (i+1) % 2 ==0:   
#            if (i+1)< const.MAX_CARD_NUM/2:
                k1+=1
            else:
                k2+=1
    return [k1, k2]


ms=datetime.now().microsecond
random.seed(ms)

cards=[]

for i in range(1, const.MAX_CARD_NUM+1):
    _card= card(0.0, i)
    cards.append(_card)

print("Try %d times, %d cards" % (const.MAX_TRY, const.MAX_CARD_NUM))
print("Try \t 0:4 \t 1:3 \t 2:2")
for i in range(1,const.MAX_TRY+1):
    for _card in cards:
        _card.x= random.random()*1.
    
    cards.sort(key=lambda c: c.x, reverse=False)
    
    kings= countKing(cards)
    king1=kings[0]
    king2=kings[1]

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

