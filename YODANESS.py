'''

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
