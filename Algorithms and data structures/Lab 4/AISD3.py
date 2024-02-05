from AISD1 import nowe_podejscie
from AISD2 import rabin_karp_macierz
import time

test = [1000, 2000, 3000, 4000, 5000, 8000]

for i in test:

    print("dla tablicy", str(i) + "x" + str(i))
    file1 = open(f"{i}_pattern.txt")
    pattern = list()


    for line in file1:
        pattern.append(line)

    time1 = time.time()
    counter, position = nowe_podejscie(pattern)
    time2 = time.time()
    print("Ilość wystąpień naiwny:", counter)
    print("czas wykonania naiwny", time2 - time1)

    file1.close()

    file2 = open(f"{i}_pattern.txt")
    txt = list()
    pattern = 'ABC'

#szybszy kod test

    for line in file2:
        pom = [letter for letter in line.rstrip('\n')]
        txt.append(pom)

    time1 = time.time()
    counter, position = rabin_karp_macierz(pattern, txt)
    time2 = time.time()

    print("Ilość wystąpień rabin krap:", counter)
    print("czas wykonania rabin krap", time2 - time1)
    print()

    file2.close()