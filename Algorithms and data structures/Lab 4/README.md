### Let's consider a two-dimensional pattern searching problem in text. Assume that the available alphabet consists of hexadecimal code symbols, i.e., P ={0,1,2,3,4,5,6,7,8,9, A, B, C, D, E, F}, and the sought pattern has the following form:

![image](https://github.com/ziobrowskipiotr/Python_projects/blob/Python/Algorithms%20and%20data%20structures/Lab%204/img.png?raw=true)


### So, we are looking for all occurrences of the sequence ABC horizontally and vertically, which share the symbol A. To test the algorithm, please use the attached text files: N_pattern.txt (where N denotes the size of the NxN symbol matrix, N = 1000, 2000, 3000, 4000, 5000, 8000).

# Task 1
### Implement the naive two-dimensional pattern search algorithm in the text. Use a 1000x1000 matrix for testing.

# Task 2
### Implement the Karp-Rabin two-dimensional pattern search algorithm in the text. Use a 1000x1000 matrix for testing.

# Task 3
### Compare the execution times of the pattern search algorithms from tasks 1 and 2 for symbol matrices N = 1000, 2000, 3000, 4000, 5000, (8000 for those interested). For each file, count the number of pattern occurrences. Which algorithm performed better? Analyze the results in comparison with the computational complexity of the algorithms discussed in the lecture. Record your findings in the report.
