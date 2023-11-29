
historia = {}

magazyn = {}


print("Witaj w programie Accountant.")

koniec_programu = False

saldo = int(input("Podaj poczatkowe saldo: "))

while not koniec_programu:
    wybor_akcji = input("Podaj rodzaj akcji ktora chcesz wykonac: ")

    if wybor_akcji == "saldo":
        zmiana_na_koncie_firmy_wyrażona_w_groszach = int(input("Podaj zmiane na koncie firmy wyzrazona w groszach: "))
        komentarz_do_zmiany = input("Podaj komentarz do zmiany: ")

        historia[zmiana_na_koncie_firmy_wyrażona_w_groszach] = komentarz_do_zmiany

        print(historia)

    elif wybor_akcji == "zakup":

        nazwa_produktu = input("Podaj identyfikator produktu:")

        cena_jednostkowa = int(input("Podaj cene jednostkowa produktu:"))

        liczba_sztuk = int(input("Podaj liczbe sztuk produktu:"))

        saldo -= cena_jednostkowa*liczba_sztuk
        if saldo < 0:
            print("Jestes na minusie.")
            break

        if nazwa_produktu in magazyn:
            magazyn[nazwa_produktu] += liczba_sztuk
        else:
            magazyn[nazwa_produktu] = liczba_sztuk
        print(magazyn)

    elif wybor_akcji == "sprzedaz":
        nazwa_produktu = input("Podaj identyfikator produktu:")

        cena_jednostkowa = int(input("Podaj cene jednostkowa produktu:"))

        liczba_sztuk = int(input("Podaj liczbe sztuk produktu:"))

        if nazwa_produktu in magazyn and magazyn[nazwa_produktu] >= liczba_sztuk:
            saldo += cena_jednostkowa * liczba_sztuk
            magazyn[nazwa_produktu] -= liczba_sztuk
            print(magazyn)

        else:
            print("Nie masz wystarczajacej ilosci produktu.")
            break

    elif wybor_akcji == "magazyn":
            print(f' Stany magazynowe: {magazyn}')
            break

    elif wybor_akcji == "konto":
        print(f'Stan konta po wszystkich akcjach: {saldo}')
        break

    elif wybor_akcji == "przegad":
        pass

    else:
        koniec_programu = True
        print("Error. Nie ma takiej akcji. Program Accountant zakonczyl dzialanie.")
