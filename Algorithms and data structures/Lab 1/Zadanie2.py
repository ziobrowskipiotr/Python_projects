import random
import time

n = 2000
A = [random.randint(0,n) for number in range(n)]
number_of_iteration = 200

def mergesort(A, a, b):
    if a < b:
        c = (a+b)//2
        mergesort(A, a, c)
        mergesort(A, c+1, b)
        merge(A, a, c, b)

def merge(T, a, c, b):
    n1 = c - a + 1
    n2 = b - c
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0 , n1):
        L[i] = T[a + i]
    for j in range(0 , n2):
        R[j] = T[c + 1 + j]
    i = 0; j = 0; k = a
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            T[k] = L[i]
            i += 1
        else:
            T[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        T[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        T[k] = R[j]
        j += 1
        k += 1

times = []
for i in range(number_of_iteration):
    start_time = time.time()
    mergesort(A, 0, len(A)-1)
    end_time = time.time()
    czas = end_time - start_time
    times.append(czas)

print("Maximum time:", max(times))
print("Minimum time:", min(times))
medium_time = sum(times)/len(times)
print("Medium time:", medium_time)