#Zadanie 7.37

base = {}
x = True

while (x != '0'):

    print('Menu wyboru:')
    print('[1] Dodaj klucz')
    print('[2] Usun klucz')
    print('[3] Szukaj klucza')
    print('[4] Wyswietl aktualna baze')
    print('[0] Wyjdz z programu\n')
    x = input('Twoj wybor: ')

    if x == '1':
        key = input('Podaj nazwe klucza: ')
        if key in base:
            print('Podany klucz juz istnieje')
            y = input('Czy chcesz go zastapic? Y/N ')
            if y == 'N':
                continue
            elif y == 'Y':
                dictionary = input('Podaj slownik do klucza: ')
                base.update({key : dictionary})
                base[key] = dictionary
            else:
                print('Podales nieprawidlowa wartosc...')
        else:
            dictionary = input('Podaj slownik do klucza: ')
            base.update({key : dictionary})
            base[key] = dictionary
    elif x == '2':
        z = input('Podaj nazwe klucza, ktory chcesz usunac: ')
        if z in base:
            del base[z]
        else:
            print('Klucz nie istnieje')
    elif x == '3':
        z = input('Podaj nazwe szukanego klucza: ')
        if z in base:
            print('Wynik wyszukiwania:',z,':', base[z])
            input('Wcisnij dowolny klawisz aby kontynuwoac')
        else:
            print('Taki klucz nie istnieje w bazie')
    elif x == '4':
        print('Twoej aktualny slownik:')
        print(base)
        print("\n")
    elif x == '0':
        print('Bye bye')
    else:
        print('Podales nieprawidlowa wartosc')




