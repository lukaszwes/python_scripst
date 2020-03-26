print('Program sprawdza, czy podana liczba jest liczba pierwsza.\n')

cont = 'Y'

while cont == 'Y':
    
    x = int(input('Podaj liczbe: '))
    if x == 2 or x == 3 or x == 5 or x == 7:
        print('Liczba', x, 'jest liczba pierwsza')

    elif x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0:
        print('Liczba', x, 'jest liczba pierwsza')

    else:
        print('Liczba', x, 'nie jest liczba pierwsza')

    cont = input('Czy chcesz kontynuowac? (Y/N): ')
    


