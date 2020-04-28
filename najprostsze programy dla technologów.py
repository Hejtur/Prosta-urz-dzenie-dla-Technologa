print('To jest pierwszy prosty program do obliczania ubytków i wydajności w przetwórstwie mięsnym')

print('\n')

print('\n')

print('Poniżej widzisz menu, które oprowadzi Cię po tym programie')

print('\n')

while(True):

    print('Wybierz 1 aby obliczyć wydajność końcową')

    print('\n')

    print('Wybierz 2 aby obliczyć kolejne ubytki')

    print('\n')

    print('Wybierz 3 aby zakończyć program')

    print('\n')
    
    wybor = input('Wpisz numer polecenia, które chcesz wykonać: ')
    
    if (wybor == '1'):
        wagaPoczatkowa = int(input('Podaj wagę początkową produktu: '))
        wagaKoncowa = int(input('Podaj wagę końcową produktu: '))
        print(wagaKoncowa / wagaPoczatkowa * 100,'%','- Taka jest wydajność końcowa')

    elif (wybor == '2'):
        while(True):
            print('Wciśnij 1 aby cofnąć się do menu startowego')
            print('Wciśnij 2 aby rozpocząć obliczanie ubytków')
            wybor2 = input('Wpisz numer polecenia, które chcesz wykonać: ')
            if (wybor2 == '1'):
                break
            elif (wybor2 == '2'):
                print('Dla ilu procesów chcesz obliczać ubytki: ')
                wybor3 = int(input('Podaj liczbę procesów, którym został poddany produkt: '))
                for wybor3 in range(wybor3):
                    wagaZPoczatkuProcesu = int(input('Podaj wagę początkową dla procesu: '))
                    wagaNaKoniecProcesu = int(input('Podaj wagę końcową dla procesu: '))
                    print(wagaZPoczatkuProcesu / wagaNaKoniecProcesu * 100 - 100, '%', '-oto ubytek w tym procesie')

    elif (wybor == '3'):
        break

    else:
        print('Proszę wybrać cyfrę: 1 lub 2 lub 3')


    print('\n')

