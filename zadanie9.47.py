#Zadanie 9.47
#Zadanie: Program liczacy pole figury
# na poczatku wybierasz figure: /prostokat/kwadrat/trojkat/trapez/kolo


import funkcje


print('Program liczy pole wybranej przez uzytkownika figury')

while (True):

    print('''\nWybierz figure:
    [1] Prosokat
    [2] Kwadrat
    [3] Trojkat
    [4] Trapez
    [5] Kolo
    [0] Wyjdz z programu''')

    x = input('Twoj wybor: ')

    if x =='1':
        a = int(input('Podaj pierwszy bok prostokata: '))
        b = int(input('Podaj drugi bok prostokata: '))
        print('Pole prostokata wynosi', funkcje.poleProstokata(a,b))
    elif x =='2':
        a = int(input('Podaj bok kwadratu: '))
        print('Pole kwadratu wynosi', funkcje.poleKwadratu(a))
    elif x =='3':
        a = int(input('Podaj podsatwe trojkata: '))
        h = int(input('Podaj wysokosc trojkata: '))
        print('Pole trojkata wynosi', funkcje.poleTrojkata(a, h))
    elif x =='4':
        a = int(input('Podaj pierwsza podstawe trapezu: '))
        b = int(input('Podaj druga podstawe trapezu: '))
        h = int(input('Podaj wysokosc trapezu: '))
        print('Pole trapezu wynosi', funkcje.poleTrapezu(a, b, h))
    elif x =='5':
        r = int(input('Podaj promien kola: '))
        print('Pole kola wynosi', funkcje.poleKola(r))
    elif x == '0':
        print('Koniec programu')
        break
    else:
        print('Dokonales zlego wyboru, sprobuj jeszcze raz')


