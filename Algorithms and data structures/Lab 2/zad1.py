import time

def hanoi(n, sour, dest, buff):
    if n == 1:
        print('z', sour, 'przeniesiono do', dest)
        return 1
    else:
        ruchy = hanoi(n - 1, sour, buff, dest)
        ruchy += hanoi(1, sour, dest, buff)
        ruchy += hanoi(n - 1, buff, dest, sour)
        return ruchy

print("Wpisz liczbę naturalną różną od 0:")
n = int(input())
start_time = time.time()
step = hanoi(n, '1', '2', '3')
end_time = time.time()
print('liczba przesunięć:', step)
print(end_time - start_time)