import random
import time

n = 2000
A = [random.randint(0,n) for number in range(n)]
number_of_iteration = 200

def insertionsort(A):
    for i in range(1, len(A)-1):
        x = A[i]
        j = i - 1
        while j >= 0 and A[j] > x:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = x

times = []
for i in range(number_of_iteration):
    start_time = time.time()
    insertionsort(A)
    end_time = time.time()
    czas = end_time - start_time
    times.append(czas)

print("Maximum time:", max(times))
print("Minimum time:", min(times))
medium_time = sum(times) / len(times)
print("Medium time:", medium_time)