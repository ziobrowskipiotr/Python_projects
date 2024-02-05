import time

def hanoi(n, sour, dest, buff):

    sterta1 = [x for x in range(n, 0, -1)]
    sterta2 = []
    sterta3 = []
    if n % 2 == 0:
        dest, buff = buff, dest


    moves = pow(2, n) - 1

    for i in range(1, moves + 1):
        if i % 3 == 1:
            if len(sterta2) == 0:
                sterta2.append(sterta1[-1])
                sterta1.pop()
                print('z', sour, 'przeniesiono do', dest)
            elif len(sterta1) == 0:
                sterta1.append(sterta2[-1])
                sterta2.pop()
                print('z', dest, 'przeniesiono do', sour)
            elif sterta1[-1] < sterta2[-1]:
                sterta2.append(sterta1[-1])
                sterta1.pop()
                print('z', sour, 'przeniesiono do', dest)
            else:
                sterta1.append(sterta2[-1])
                sterta2.pop()
                print('z', dest, 'przeniesiono do', sour)

        if i % 3 == 2:
            if len(sterta3) == 0:
                sterta3.append(sterta1[-1])
                sterta1.pop()
                print('z', sour, 'przeniesiono do', buff)
            elif len(sterta1) == 0:
                sterta1.append(sterta3[-1])
                sterta3.pop()
                print('z', buff, 'przeniesiono do', sour)
            elif sterta1[-1] < sterta3[-1]:
                sterta3.append(sterta1[-1])
                sterta1.pop()
                print('z', sour, 'przeniesiono do', buff)
            else:
                sterta1.append(sterta3[-1])
                sterta3.pop()
                print('z', buff, 'przeniesiono do', sour)

        if i % 3 == 0:
            if len(sterta3) == 0:
                sterta3.append(sterta2[-1])
                sterta2.pop()
                print('z', buff, 'przeniesiono do', dest)
            elif len(sterta2) == 0:
                sterta2.append(sterta3[-1])
                sterta3.pop()
                print('z', dest, 'przeniesiono do', buff)
            elif sterta2[-1] < sterta3[-1]:
                sterta3.append(sterta2[-1])
                sterta2.pop()
                print('z', dest, 'przeniesiono do', buff)
            else:
                sterta2.append(sterta3[-1])
                sterta3.pop()
                print('z', buff, 'przeniesiono do', dest)
    return moves

print("Wpisz liczbę naturalną różną od 0:")
n = int(input())
start_time = time.time()
moves = hanoi(n, 'A', 'B', 'C')
end_time = time.time()
print('liczba przesunięć:', moves)
print(end_time - start_time)