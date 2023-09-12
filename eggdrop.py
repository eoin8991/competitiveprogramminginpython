'''
Egg Drop

Problem:

Imagine that you are in a building with F floors (starting at floor 1, the lowest floor), and you have a
large number of identical eggs, each in its own identical protective container. For each floor in the
building, you want to know whether or not an egg dropped from that floor will break. If an egg
breaks when dropped from floor i, then all eggs are guaranteed to break when dropped from any
floor j ≥ i. Likewise, if an egg doesn't break when dropped from floor i, then all eggs are guaranteed
to never break when dropped from any floor j ≤ i.

We can define Solvable(F, D, B) to be true if and only if there exists an algorithm to determine
whether or not an egg will break when dropped from any floor of a building with F floors, with the
following restrictions: you may drop a maximum of D eggs (one at a time, from any floors of your
choosing), and you may break a maximum of B eggs. You can assume you have at least D eggs in
your possession.

Input
The first line of input gives the number of cases, 1 ≤ N ≤ 100. N test cases follow. Each
case is a line formatted as:
F D B
Solvable(F, D, B) is guaranteed to be true for all input cases.

Output
For each test case, output one line containing "Case #x: " followed by three space-separated
integers: Fmax, Dmin, and Bmin. The definitions are as follows:
•Fmax is defined as the largest value of F' such that Solvable(F', D, B) is true, or -1 if this
value would be greater than or equal to 232 (4294967296).
(In other words, Fmax
= -1 if and only if Solvable(232, D, B) is true.)
•Dmin is defined as the smallest value of D' such that Solvable(F, D', B) is true.
•Bmin is defined as the smallest value of B' such that Solvable(F, D, B') is true.
Sample Input
2
3 3 3
7 5 3
Sample Output
Case #1: 7 2 1
Case #2: 25 3 2
'''

import sys
import numpy as np

class EggDrop:
    def __init__(self, is, os):
        self.scanner = sys.stdin
        self.writer = sys.stdout

    MAX_F_VALUE = 4294967296
    LARGE_F_VALUE = -1
    MAX_B_INDEX = 32
    F_CACHE_SIZE = 100000

    def solve(self):
        self.fCache = np.zeros((self.F_CACHE_SIZE, self.MAX_B_INDEX), dtype=np.int64)
        self.initFCache()
        n = int(input())
        for i in range(1, n+1):
            F = int(input())
            D = int(input())
            B = int(input())
            self.writer.write("Case #")
            self.writer.write(str(i) + ": ")
            Fmax = self.getF(D, B)
            Dmin = self.getD(F, B, D)
            Bmin = self.getB(F, D, B)
            self.writer.write("{} {} {}\n".format(Fmax, Dmin, Bmin))

    def getF(self, d, b):
        if b > self.MAX_B_INDEX:
            b = self.MAX_B_INDEX
        if b == 1:
            return d
        if d > self.F_CACHE_SIZE:
            return -1
        return self.fCache[d - 1][b - 1]

    def getD(self, f, b, dMax):
        for d in range(1, dMax+1):
            maxF = self.getF(d, b)
            if (maxF == self.LARGE_F_VALUE) or (maxF >= f):
                return d
        raise ValueError("D not found, F={}, B={}, Dmax={}".format(f, b, dMax))

    def getB(self, f, d, bMax):
        for b in range(1, bMax+1):
            maxF = self.getF(d, b)
            if (maxF == self.LARGE_F_VALUE) or (maxF >= f):
                return b
        raise ValueError("B not found, F={}, D={}, max B={}".format(f, d, bMax))

    def initFCache(self):
        self.fCache[0] = np.ones(self.MAX_B_INDEX, dtype=np.int64)
        for d in range(1, self.F_CACHE_SIZE):
            self.fCache[d][0] = d + 1
            for b in range(1, self.MAX_B_INDEX):
                if (self.fCache[d - 1][b] == self.LARGE_F_VALUE) or (self.fCache[d - 1][b - 1] == self.LARGE_F_VALUE):
                    self.fCache[d][b] = self.LARGE_F_VALUE
                else:
                    self.fCache[d][b] = self.fCache[d - 1][b] + 1 + self.fCache[d - 1][b - 1]
                    if self.fCache[d][b] >= self.MAX_F_VALUE:
                        self.fCache[d][b] = self.LARGE_F_VALUE

eggDrop = EggDrop(sys.stdin, sys.stdout)
eggDrop.solve()

'''
code development inspiration from illya-keeplearning
'''
