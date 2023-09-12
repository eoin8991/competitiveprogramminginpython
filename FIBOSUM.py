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

MOD = 1000000007

def multiply(F, M):
    x = (F[0][0] * M[0][0] + F[0][1] * M[1][0]) % MOD
    y = (F[0][0] * M[0][1] + F[0][1] * M[1][1]) % MOD
    z = (F[1][0] * M[0][0] + F[1][1] * M[1][0]) % MOD
    w = (F[1][0] * M[0][1] + F[1][1] * M[1][1]) % MOD
    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w

def power(F, n):
    if n == 0 or n == 1:
        return
    M = [[1, 1], [1, 0]]
    power(F, n // 2)
    multiply(F, F)
    if n % 2 != 0:
        multiply(F, M)

def fib(n):
    F = [[1, 1], [1, 0]]
    if n == 0:
        return 0
    power(F, n - 1)
    return F[0][0]

t = int(input())
while t > 0:
    n, m = map(int, input().split())
    if n > m:
        print("Error!!")
    else:
        result = (fib(m + 2) - fib(n + 1)) % MOD
        if result < 0:
            result += MOD
        print(result)
    t -= 1

'''
code development inspiration from kashsingh
'''

'''
Key Concepts:
-modulo vs integer division
'''
