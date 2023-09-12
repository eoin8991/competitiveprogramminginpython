'''
Problem

FIBOSUM - Fibonacci Sum
no tags 
The Fibonacci sequence is defined by the following relation:

F(0) = 0
F(1) = 1
F(N) = F(N - 1) + F(N - 2), N >= 2
Your task is very simple. Given two non-negative integers N and M, you have to 
calculate the sum (F(N) + F(N + 1) + ... + F(M)) mod 1000000007.

Input
The first line contains an integer T (the number of test cases). Then, T lines follow. 
Each test case consists of a single line with two non-negative integers N and M.

Output
For each test case you have to output a single line containing the answer for the task.

Example
Input:
3
0 3
3 5
10 19

Output:
4
10
10857

Constraints
T <= 1000
0 <= N <= M <= 109
'''
