#War card game

import random
from enum import IntEnum

cardList = ["9", "9", "9", "9",
         "10", "10", "10", "10",
         "Jack", "Jack", "Jack", "Jack",
         "Queen", "Queen", "Queen", "Queen",
         "King", "King", "King", "King",
         "Ace", "Ace", "Ace", "Ace",
         "Joker", "Joker"
        ]


CardValue = IntEnum('CardValue', '9 10 Jack Queen King Ace Joker')



def tasowanie(cards):
    random.shuffle(cards)

def rozdanie(cards):
    gracz1 = []
    gracz2 = []
    while len(cards) > 0:
        gracz1.append(cards.pop())
        gracz2.append(cards.pop())
    return gracz1, gracz2

tasowanie(cardList)
Gracz1, Gracz2 = rozdanie(cardList)

print(Gracz1)
print(Gracz2)
stack = []
i = 0
while len(Gracz1) > 0 and len(Gracz2) > 0:
    i += 1
    if CardValue[str(Gracz1[0])] > CardValue[str(Gracz2[0])]:
        print('Partia dla Gracza 1')
        stack.append(Gracz1[0])
        stack.append(Gracz2[0])
        Gracz1.pop(0)
        Gracz2.pop(0)
        Gracz1 += stack
        stack.clear()
        print(Gracz1)
        print(Gracz2)
    elif CardValue[str(Gracz1[0])] < CardValue[str(Gracz2[0])]:
        print('Partia dla Gracza 2')
        stack.append(Gracz1[0])
        stack.append(Gracz2[0])
        Gracz1.pop(0)
        Gracz2.pop(0)
        Gracz2 += stack
        stack.clear()
        print(Gracz1)
        print(Gracz2)
    else:
        print('Remis - WOJNA!')
        stack.append(Gracz1[0])
        stack.append(Gracz2[0])
        Gracz1.pop(0)
        Gracz2.pop(0)
        print(Gracz1)
        print(Gracz2)
print('Ilosc rozdan: ',i)

   
