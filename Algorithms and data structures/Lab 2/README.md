### The Tower of Hanoi problem involves rebuilding a tower of disks with different diameters while maintaining their shape. During the transfer, it is allowed to use a buffer in the form of an additional pole. Operations are performed with the assumption that it is not allowed to place a disk with a larger diameter on top of a smaller one or move multiple disks at once.

![image](https://github.com/ziobrowskipiotr/Python_projects/blob/Python/Algorithms%20and%20data%20structures/Lab%202/img2.png?raw=true)

##### Figure 1: Visualization of the algorithm for three disks.

# Task 1
### Implement a recursive algorithm to solve the Tower of Hanoi problem. The algorithm should count the number of steps required and sequentially print the moves leading to the problem's solution. Below is an example pseudo-code representation of the algorithm, where the variable n represents the number of disks, and the variables sour, dest, buff represent the source pole, target pole, and auxiliary pole respectively.

```
Hanoi(n, sour, dest, buff):
	IF n==1 :
		Move disk from sour to dest
	Hanoi (n-1, sour, buff, dest)
	Move disk from sour to dest
	Hanoi (n-1, buff, dest, sour)
```

# Task 2
### Implement an iterative algorithm to solve the Tower of Hanoi problem. The algorithm should count the number of steps required and sequentially print the moves leading to the problem's solution. Below is the algorithm represented in pseudo-code, where the variable n represents the number of disks, and i represents the step number, while the variables sour, dest, buff represent the source pole, target pole, and auxiliary pole respectively.

```
Hanoi(n, sour, dest, buff):
	WHILE (sour != Null OR buff !=Null):
		IF i%3 == 1:
			Possible move disk between sour and dest
		IF i%3 == 2:
			Possible move disk between sour and buff
		IF i%3 == 0:
			Possible move disk between buff and dest
```
Note: It is important to check in which direction the move is possible and indicate from which pole to which the move should be made.

# Task 3
### Verify the correctness of both algorithms by comparing the moves executed sequentially and their quantity. Compare the speed of operation of both algorithms depending on the number of disks. Are both algorithms optimal (do they perform the same number of operations)? Assess which type of algorithm implementation is easier.
