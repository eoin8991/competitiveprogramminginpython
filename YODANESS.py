'''
Problem Statement:

YODANESS - Yodaness Level
#graph-theory #number-theory #shortest-path #sorting #tree #bitmasks
Yoda is the wisest, and perhaps the most powerful Jedi of his time. Yoda is a mysterious figure 
and he has many oddities. One of them is that Yoda often changes the order of words in the sentence. 
For example, one of such phrases is "Or I will help you not." Let's call the yodaness level of any statement 
the number of pairs of words that changed their order, as to the order in which they were supposed to go in 
a normal statement. Write a program that determines the yodaness level of different statement of Yoda.

 
Input
The first line of input contains the number t - the number of tests. Next comes the description of t tests. 
Each test consists of three rows. The first line of the test contains an integer n - number of words in the 
statement. The next line contains n words separated by spaces - the statement as Yoda says it. The next line 
is n words separated by spaces - the same statement as it should be said normally. All the words in the statement 
are different and consist of small latin letters.

Constraints
1 <= t <= 10
1 <= n <= 30000
the length of each word does not exceed 20 characters

Output
For each test print the yodaness level of the statement.

Example
Input:
2
6
in the force strong you are
you are strong in the force
6
or i will help you not
or i will not help you

Output:
11
2
'''

#this is the solution that comes closest
#however it gets a time limit exceeded error on SPOJ

import sys
from collections import defaultdict

MAX = 30000
strings = ["" for _ in range(MAX)]
bit = [0 for _ in range(MAX+1)]
m = defaultdict(int)
cur = ""
n = 0

def update(idx):
    while idx <= n:
        bit[idx] += 1
        idx += (idx & -idx)

def cf(idx):
    c = 0
    while idx > 0:
        c += bit[idx]
        idx -= (idx & -idx)
    return c

for _ in range(int(input())):
    m.clear()
    n = int(input())
    bit = [0 for _ in range(n+1)]
    strings = [input() for _ in range(n)]
    for i in range(1, n+1):
        cur = input()
        m[cur] = i
    j = (n*(n-1))//2
    for i in range(n):
        p = m[strings[i]]
        j -= cf(p)
        update(p)
    print(j)

'''
code inspiration credit to nikolaygurev
'''

'''
Key concepts:
-Bitwise operations using & operator
-Integer division using //
-Clearing a defaultdict
-Initializing a defaultdict
'''
