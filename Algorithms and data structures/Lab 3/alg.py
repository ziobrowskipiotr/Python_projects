import time
import random
def wyszukiwanie_binarne(list, poczatek, koniec, element):
    if koniec>=poczatek:
        srodek= (poczatek + koniec)//2
        if list[srodek].pobierz_dane() == element:
            return srodek
        elif list[srodek].pobierz_dane() > element:
            return wyszukiwanie_binarne(list,poczatek,srodek-1,element)
        else:
            return wyszukiwanie_binarne(list,srodek+1,koniec,element)
    else:
        return poczatek
def wyszukiwanie_binarne_find (list, kon, pocz, element):
    if pocz >= kon:
        mid = (kon + pocz) // 2
        if list[mid].pobierz_dane() == element:
            return mid
        elif list[mid].pobierz_dane() > element:
            return wyszukiwanie_binarne_find(list, kon, mid-1, element)
        else:
            return wyszukiwanie_binarne_find(list, mid + 1, pocz, element)
    else:
        return -1

class posortowana_tablica:
    def __init__(self):
        self.list = []
        self.roots = []

    def insert(self, element):
        dane_roota = round(element)
        if element - dane_roota >= 0:
            dane_roota += 0.5
        else:
            dane_roota -= 0.5

        znajdz_indeks = wyszukiwanie_binarne(self.list, 0, len(self.list) - 1, dane_roota)
        try:
            if self.list[znajdz_indeks].pobierz_dane() == dane_roota:
                self.list[znajdz_indeks].insert(element)
            else:
                nowy_wezel = wezel(dane_roota)
                nowy_wezel.insert(element)
                self.list.insert(znajdz_indeks, nowy_wezel)
                self.roots.insert(znajdz_indeks, nowy_wezel)
        except IndexError:
            nowy_wezel = wezel(dane_roota)
            nowy_wezel.insert(element)
            self.list.insert(znajdz_indeks, nowy_wezel)
            self.roots.insert(znajdz_indeks, nowy_wezel)



    def pokaz_drzewo(self):
        for i in self.list:
            i.pokaz_drzewo()
            print('\n')

    def minimum(self, wezel):
        index = wyszukiwanie_binarne_find(self.list, 0, len(self.list) - 1, wezel)
        if (index != -1):
            return self.list[index].minimum()
        else:
            return None

    def maximum(self, wezel):
        index = wyszukiwanie_binarne_find(self.list, 0, len(self.list) - 1, wezel)
        if (index != -1):
            return self.list[index].maximum()
        else:
            return None

    def maximum_tree(self):
        max_wezel = None
        for root in self.roots:
            wezel = root
            while wezel.right is not None:
                wezel = wezel.right
            if max_wezel is None or wezel.pobierz_dane() > max_wezel.pobierz_dane():
                max_wezel = wezel
        if max_wezel is not None:
            return max_wezel.pobierz_dane()
        else:
            return None

    def wyszukaj(self, element):
        dane_roota = round(element)
        if element - dane_roota >= 0:
            dane_roota += 0.5
        else:
            dane_roota -= 0.5

        index = wyszukiwanie_binarne_find(self.list, 0, len(self.list) - 1, dane_roota)
        return self.list[index].wyszukaj(element)
class wezel:
    def __init__(self,dane):
        self.left=None
        self.right=None
        self.dane=dane

    def pobierz_dane(self):
        return self.dane

    def insert(self,dane):
        temp_wezel = self
        while(True):
            if dane<temp_wezel.pobierz_dane():
                if temp_wezel.left:
                    temp_wezel = temp_wezel.left
                else:
                    temp_wezel.left = wezel(dane)
                    break
            elif dane > temp_wezel.pobierz_dane():
                if temp_wezel.right:
                    temp_wezel = temp_wezel.right
                else:
                    temp_wezel.right = wezel(dane)
            else:
                break

    def pokaz_drzewo(self, glebokosc=0, nowa_linia=False):
        if nowa_linia:
            print('\n' + '\t' * (glebokosc) + '-' * glebokosc + str(self.dane) + '\t', end='')
        else:
            print('-' * glebokosc + str(self.dane) + '\t', end='')

        if self.left:
            self.left.pokaz_drzewo(glebokosc + 1)

        if self.right:
            self.right.pokaz_drzewo(glebokosc + 1, True)

    def minimum(self):
        temp_wezel = self
        while (temp_wezel.left):
            temp_wezel = temp_wezel.left

        return (temp_wezel.pobierz_dane())

    def maximum(self):
        temp_wezel = self
        while (temp_wezel.right):
            temp_wezel = temp_wezel.right

        return (temp_wezel.pobierz_dane())

    def wyszukaj(self, element):
        temp_wezel = self
        while (temp_wezel):
            if temp_wezel.pobierz_dane() < element:
                temp_wezel = temp_wezel.right
            elif temp_wezel.pobierz_dane() > element:
                temp_wezel = temp_wezel.left
            else:
                return True

        return False


if __name__ == '__main__':

     #Zadanie1

    nowa_tablica1=posortowana_tablica()
    nowa_tablica1.insert(1.3)
    nowa_tablica1.insert(1.6)
    nowa_tablica1.insert(3.7)
    nowa_tablica1.insert(4.0)
    nowa_tablica1.insert(4.99)
    nowa_tablica1.insert(7.3)
    nowa_tablica1.insert(7.8)
    nowa_tablica1.insert(7.7)
    nowa_tablica1.insert(7.9)
    nowa_tablica1.insert(7.6)
    nowa_tablica1.insert(9.3)
    nowa_tablica1.pokaz_drzewo()

    #Zadanie 2

    print(nowa_tablica1.wyszukaj(1.3))
    print(nowa_tablica1.wyszukaj(3.9))
    print("minimalna wartosc dla korzenia = 1.5:", nowa_tablica1.minimum(1.5))
    print("maksymalna wartosc dla korzenia = 1.5: ", nowa_tablica1.maximum(1.5))
    print("najwieksza wartosc w calym drzwie: ", nowa_tablica1.maximum_tree())

    #Zadanie 3

    nowa_tablica1 = posortowana_tablica()
    nowa_tablica2 = posortowana_tablica()
    nowa_tablica3 = posortowana_tablica()
    nowa_tablica4 = posortowana_tablica()

    steps = [25, 50, 100, 1000, 5000]
    for iterations in steps:
        nowa_tablica5 = posortowana_tablica()
        nowa_tablica2 = posortowana_tablica()
        nowa_tablica3 = posortowana_tablica()
        nowa_tablica4 = posortowana_tablica()
        start_s = time.time()
        for i in range(iterations, 0, -1):
            nowa_tablica5.insert(i)

        print("liczba iteracji: " + str(iterations) + ", czas trwania: " + str(time.time() - start_s))

        start_nowa_tablica3 = time.time()
        for i in range(iterations):
            i = round(random.random() * 10, 2)
            nowa_tablica2.insert(i)

        print("liczba iteracji: " + str(iterations) + ", czas trwania:" + str(time.time() - start_nowa_tablica3))

        start_r = time.time()
        for i in range(iterations):
            i = round(random.random() * 100, 2)
            nowa_tablica3.insert(i)

        print("liczba iteracji: " + str(iterations) + ", czas trwania:" + str(time.time() - start_r))

        start_max = time.time()
        for i in range(10000):
            i = random.randint(0, 99) + 0.5
            nowa_tablica3.maximum(i)

        print("max, " + str(iterations) + ", " + str(time.time() - start_max))

        start_min = time.time()
        for i in range(10000):
            i = random.randint(0, 99) + 0.5
            nowa_tablica3.minimum(i)

        print("min, " + str(iterations) + ", " + str(time.time() - start_min))

        start_wyszukaj = time.time()
        for i in range(10000):
            i = random.randint(0, 99) + 0.5
            nowa_tablica3.wyszukaj(i)

        print("wyszukiwanie, " + str(iterations) + ", " + str(time.time() - start_min))