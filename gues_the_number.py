#Zadanie 5.26

import random

print('Zgadnij sekretna liczbe\n')

liczba = int(round(random.uniform(0,100),0))
x = 'zero'
first = True


while x != liczba:
    if first == True:
        x = int(input('Podaj sekretna liczbe: '))
        first = False
    else:
        x = int(input('Sprobuj jeszcze raz: '))
        
    if x < liczba:
        print('Podales za mala liczbe.')
    elif x > liczba:
        print('Podlaes za duza liczbe.')
    elif x == liczba:
        print('Brawo Ty!')
    else:
        continue





