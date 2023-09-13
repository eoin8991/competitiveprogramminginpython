'''
Problem

The original ICParchive 8154 frosting on the cake question has been erased from the internet for the most part.
It seems to be similar to this UVA 13291 question, found here:
https://www.udebug.com/UVa/13291
https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=878&page=show_problem&problem=5215

Iskander the Baker is decorating a huge
cake, covering the rectangular surface of
the cake with frosting. For this purpose,
he mixes frosting sugar with lemon juice
and food coloring, in order to produce
three kinds of frosting: yellow, pink, and
white. These colors are identified by the
numbers 0 for yellow, 1 for pink, and 2 for
white.
To obtain a nice pattern, he partitions the cake surface into vertical stripes
of width A1, A2, . . . , An centimeters, and
horizontal stripes of height B1, B2, . . . , Bn
centimeters, for some positive integer n.
These stripes split the cake surface into
n × n rectangles. The intersection of vertical stripe i and horizontal stripe j has
color number (i + j) mod 3 for all 1 ≤
i, j ≤ n. To prepare the frosting, Iskander
wants to know the total surface in square
centimeters to be colored for each of the
three colors, and asks for your help.
Input
The input file contains several test cases, each of them as described below.
The input consists of the following integers:
• on the first line: the integer n,
• on the second line: the values of A1, . . . , An, n integers separated with single spaces,
• on the third line: the values of B1, . . . , Bn, n integers separated with single spaces.
Limits
The input satisfies 3 ≤ n ≤ 100 000 and 1 ≤ A1, . . . , An, B1, . . . , Bn ≤ 10 000.
Output
For each test case, the output must follow the description below.
The output should consist of three integers separated with single spaces, representing the total area
for each color 0, 1, and 2.
Sample Input
3
1 1 1
1 1 1
7
6 2 4 5 1 1 4
2 5 1 4 2 3 4
Sample Output
3 3 3
155 131 197
'''

import sys

for line in sys.stdin:
    n = int(line)
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    white = 0
    pink = 0
    yellow = 0
    
    for i in range(1, n + 1):
        a[i] = int(input())
        if i % 3 == 0:
            pink += a[i]
        if i % 3 == 1:
            yellow += a[i]
        if i % 3 == 2:
            white += a[i]
    
    Y = 0
    W = 0
    P = 0
    
    for i in range(1, n + 1):
        b[i] = int(input())
        if i % 3 == 2:
            W += b[i] * white
            Y += b[i] * yellow
            P += b[i] * pink
        elif i % 3 == 1:
            Y += b[i] * white
            P += b[i] * yellow
            W += b[i] * pink
        else:
            P += b[i] * white
            W += b[i] * yellow
            Y += b[i] * pink
    
    print(Y, W, P)

'''
code development inspiration from mdnooruddin
'''

'''
Key Concepts:
-sys.stdin can used directly as input for a loop
-initializing lists by a = [x] * number
-modifying lists by their index number eg a[i]
'''
