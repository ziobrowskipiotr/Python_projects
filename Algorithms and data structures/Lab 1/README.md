# Task 1
### Implement the insertion sort algorithm for a sequence of length n.
```
insertionsort(A)
for i = 1 to length(A) - 1
	x = A[i]
	j = i - 1
	while j >= 0 and A[j] > x
		A[j+1] = A[j]
		j = j - 1
	A[j+1] = x
End
```

# Task 2
### Implement the merge sort algorithm for a sequence A of length n. The merge function is used to merge two sorted sequences into one sorted sequence of numbers.
```
mergesort(A, a,b)
	if a < b:
		c = (a+b)/2
		mergesort(A, a,c)
		mergesort(A, c+1, b)
		merge(T, a, c, b)
End
```
# Task 3
### Compare the computational time complexity of the insertion sort and merge sort algorithms. To obtain reliable results, perform multiple (>10^2) iterations. In each iteration, generate a sequence of constant length (>10^3). Measure the execution time for both algorithms across all iterations, record the fastest and slowest iteration times, and calculate the average iteration execution time. When implementing the merge sort, pay attention to the limitations of stack size, which can affect the number of possible recursion levels.
