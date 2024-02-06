### Let's consider a data structure where the root is an array of length N, and each element of this array is the root of a subtree. Subtrees are created following the definition of binary search trees. Assume that each element in the array (the roots) stores numbers from 0.5 to +∞ with a step of 1.0, while the subtrees store fractional numbers (with a precision of 0.01) that are not farther than 0.5 from the value of the root on the number line.

![image](https://github.com/ziobrowskipiotr/Python_projects/blob/Python/Algorithms%20and%20data%20structures/Lab%203/img1.png?raw=true)


### Figure 1: Example of the discussed data structure.
### This presented structure efficiently allows for storing disjoint, unsorted sets of data. Do you know any use cases where it could find application? (Write your answer in the report.)

# Task 1
### Implement the data structure described in the introduction and a tool for textual data visualization in the manner shown below:
```
1.5-1.3
   -1.6
3.5-3.7
4.5-4.0
   -4.99
7.5-7.3
   -7.8--7.7---7.6
       --7.9
9.5-9.3
```
### Elements on the same level should be placed in the same column. Subsequent levels are separated by a number of '-' characters corresponding to the level of nesting. To present the visualization, populate the structure with sample data.

# Task 2
### Please assume the initial state of the structure according to the example in Fig. 1. Implement the following operations:
- INSERT(x) - insert a node with value x according to the structure's assumptions.
- MINIMUM(y) - find the minimum value node in the entire structure.
- MAXIMUM(y) - find the maximum value node in the entire structure.
- SEARCH(x) - check if a node with the value x is stored in the structure.

# Task 3
### Check the execution time of all operations from task 2 for a structure containing, for example, 25, 50, 100, 500, and 1000 elements (random data). Estimate their computational complexity.
