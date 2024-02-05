def nowe_podejscie(wzorzec):
    pozycje = []
    licznik = 0

    for wiersz in range(len(wzorzec)):
        for kolumna in range(len(wzorzec[0])):
            try:
                poziomo = wzorzec[wiersz][kolumna:kolumna+3]
                pionowo = wzorzec[wiersz][kolumna] + wzorzec[wiersz+1][kolumna] + wzorzec[wiersz+2][kolumna]
                if poziomo == pionowo == 'ABC':
                    pozycje.append([wiersz, kolumna])
                    licznik += 1
            except IndexError:
                pass
    return licznik, pozycje