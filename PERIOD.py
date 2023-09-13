'''
Problem

PERIOD - Period
no tags 
For each prefix of a given string S with N characters (each character has an ASCII code between 
97 and 126, inclusive), we want to know whether the prefix is a periodic string. That is, for each i (2 <= i <= N) we want to 
know the largest K > 1 (if there is one) such that the prefix of S with length i can be written as AK , that is A concatenated K 
times, for some string A. Of course, we also want to know the period K.

Input
The first line of the input file will contains only the number T (1 <= T <= 10) of the test cases.

Each test case consists of two lines. The first one contains N (2 <= N <= 1 000 000) – the size of the string S. The second line contains the string S.

Output
For each test case, output “Test case #” and the consecutive test case number on a single line; then, for each prefix with length i that has a period 
K > 1, output the prefix size i and the period K separated by a single space; the prefix sizes must be in increasing order. Print a blank line after each test case.

Example
Input:
2
3
aaa
12
aabaabaabaab

Output:
Test case #1
2 2
3 3

Test case #2
2 2
6 2
9 3
12 4

'''

import sys
import re
from collections import deque
from collections import defaultdict
from collections import Counter
from math import sqrt
from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import accumulate
from functools import reduce
from operator import add
from operator import mul
from operator import itemgetter
from operator import attrgetter
from operator import methodcaller
from heapq import heappush
from heapq import heappop
from bisect import bisect_left
from bisect import bisect_right
from bisect import bisect
from fractions import gcd
from fractions import Fraction
from decimal import Decimal
from decimal import getcontext
from decimal import ROUND_HALF_UP
from decimal import ROUND_HALF_EVEN
from decimal import ROUND_DOWN
from decimal import ROUND_UP
from decimal import ROUND_CEILING
from decimal import ROUND_FLOOR
from decimal import ROUND_05UP
from decimal import ROUND_HALF_DOWN
from decimal import ROUND_05DOWN
from decimal import ROUND_HALF_CEILING
from decimal import ROUND_HALF_FLOOR
from decimal import ROUND_HALF_ODD
from decimal import ROUND_05CEILING
from decimal import ROUND_05FLOOR
from decimal import ROUND_05ODD
from decimal import ROUND_HALF_EVEN
from decimal import ROUND_HALF_UP
from decimal import ROUND_DOWN
from decimal import ROUND_UP
from decimal import ROUND_CEILING
from decimal import ROUND_FLOOR
from decimal import ROUND_05UP
from decimal import ROUND_HALF_DOWN
from decimal import ROUND_05DOWN
from decimal import ROUND_HALF_CEILING
from decimal import ROUND_HALF_FLOOR
from decimal import ROUND_HALF_ODD
from decimal import ROUND_05CEILING
from decimal import ROUND_05FLOOR
from decimal import ROUND_05ODD

def checkIfPeriodic(s, n, pos):
    if n == 0:
        return
    res = pos + 1 - n
    if (pos + 1) % res != 0:
        return
    print(pos + 1, (pos + 1) // res)

def prepareLPSArray(pattern):
    len = len(pattern)
    lsp = [0] * len
    lsp[0] = 0
    j = 0
    for i in range(1, len):
        if pattern[i] == pattern[j]:
            lsp[i] = j + 1
            j += 1
        else:
            while True:
                if j == 0 or pattern[j] == pattern[i]:
                    break
                j = lsp[j-1]
            if pattern[j] == pattern[i]:
                lsp[i] = j + 1
                j += 1
            else:
                lsp[i] = 0
        if lsp[i] == 0:
            continue
        res = i + 1 - lsp[i]
        if (i + 1) % res != 0:
            continue
        print(i + 1, (i + 1) // res)

t = int(input())
cas = 1
for _ in range(t):
    n = int(input())
    s = input()
    print("Test case #{}".format(cas))
    prepareLPSArray(s)
    print()

'''
code development inspiration from jiteshsunhala
'''
