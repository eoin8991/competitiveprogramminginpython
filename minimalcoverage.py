'''
Problem

1303. Minimal Coverage
Time limit: 1.0 second
Memory limit: 64 MB

Given set of line segments [Li, Ri] with integer coordinates of their end points. Your task is to find the 
minimal subset of the given set which covers segment [0, M] completely (M is a positive integer).

Input
First line of the input contains an integer M (1 ≤ M ≤ 5000). Subsequent lines of input contain pairs of integers 
Li and Ri (−50000 ≤ Li < Ri ≤ 50000). Each pair of coordinates is placed on separate line. Numbers in the pair are 
separated with space. Last line of input data contains a pair of zeroes. The set contains at least one and at most 99999 segments.

Output
Your program should print in the first line of output the power of minimal subset of segments which covers segment [0, M]. 
The list of segments of covering subset must follow. Format of the list must be the same as described in input with exception 
that ending pair of zeroes should not be printed. Segments should be printed in increasing order of their left end point coordinate.
If there is no covering subset then print “No solution” to output.

Samples
input	
1
-1 0
-5 -3
2 5
0 0

output
No solution

input
1
-1 0
0 1
0 0

output
1
0 1
'''

import sys

inf = 200000

class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

cover = [inf] * 6000
p = [0] * 6000
seg = [Pair(0, 0)] * 100000
N = 0
M = 0

def min(a, b):
    return a if a < b else b

def max(a, b):
    return a if a > b else b

def compare(a, b):
    p1 = a
    p2 = b
    return p1.first - p2.first

def init():
    global N, M
    for i in range(N):
        cover[i] = inf
    seg.sort(key=lambda x: x.first)
    for i in range(M):
        for j in range(min(N-1, seg[i].second), seg[i].first, -1):
            if cover[j] != inf:
                break
            cover[j] = seg[i].first
            p[j] = i

sol = [Pair(0, 0)] * 100000
S = 0

def get_covering():
    global N, sol, S
    i = N - 1
    covering = 0
    while i > 0:
        if cover[i] == inf:
            return inf
        covering += 1
        sol[S] = seg[p[i]]
        S += 1
        i = cover[i]
    return covering

N = int(input())
N += 1
M = 0
seg[M].first, seg[M].second = map(int, input().split())
while seg[M].first or seg[M].second:
    M += 1
    seg[M].first, seg[M].second = map(int, input().split())
    if seg[M].first > seg[M].second:
        temp = seg[M].first
        seg[M].first = seg[M].second
        seg[M].second = temp

init()
covering = get_covering()
if covering == inf:
    print("No solution")
    sys.exit(0)
print(covering)
for i in range(S-1, -1, -1):
    print(sol[i].first, sol[i].second)
sys.exit(0)

'''
code solution inspiration from marioyc
'''

'''
Key Concepts:
-defining a class by initializing attributes through __init__()
-sorting using the lambda function
-exiting a system using sys.exit(0)
'''
