def rabin_karp_macierz(wzorzec, macierz):
    m = len(wzorzec)
    wiersze = len(macierz)
    kolumny = len(macierz[0])
    licznik = 0
    pozycje = []
    hash_wzorca = hash(wzorzec)
    pom = 0

    for wiersz in macierz:
        wiersz_str = ''.join(wiersz)
        n = len(wiersz_str)

        hash_wiersza = hash(wiersz_str[:m])

        for i in range(n - m + 1):
            if hash_wiersza == hash_wzorca and wiersz_str[i:i+m] == wzorzec:
                try:
                    kolumna = macierz[pom][i] + macierz[pom + 1][i] + macierz[pom + 2][i]
                    if kolumna == wzorzec:
                        licznik += 1
                        pozycje.append([pom, i])
                except IndexError:
                    continue

            if i < n - m:
                hash_wiersza = hash(wiersz_str[i+1:i+m+1])
        pom += 1
    return licznik, pozycje