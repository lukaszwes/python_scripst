print('Ciag Fibonacciego\n')

while True:
    try:
        x = int(input('Podaj maksymalna wartosc ciagu: '))
        while x<1:
            print('Podales nieprawidlowa wartosc, sprobuj jeszcze raz...')
            x = int(input('Podaj maksymalna wartosc ciagu: '))
        break
    except ValueError:
        print('Nie podales liczby calkowitej, sprobuj jeszcze raz...')

fibo = [0,1]
i = 0

while True:
    if fibo[i]+fibo[i+1] <= x:
        fibo.append(fibo[i]+fibo[i+1])
        i += 1
    else:
        break

print('\nWygenerowany ciag Fibonacciego:')



def shift_left(tab):
    conv = []
    for i in range(1,len(tab)):
        conv.append(tab[i])
    conv.append(tab[0])
    return conv

print('Original:\t',fibo)
print('One left shift:\t',shift_left(fibo))

