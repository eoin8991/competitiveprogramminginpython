'''
Enormous Input Test

The purpose of this problem is to verify whether the method you are using to read input data 
is sufficiently fast to handle problems branded with the enormous Input/Output warning. You are 
expected to be able to process at least 2.5MB of input data per second at runtime.

Input

The input begins with two positive integers n k (n, k<=107). The next n lines of input contain one 
positive integer ti, not greater than 109, each.

Output

Write a single integer to output, denoting how many integers ti are divisible by k.

Example

Input:
7 3
1
51
966369
7
9
999996
11

Output:
4
'''

import sys

n, k = input().split()
n = eval(n)
k = eval(k)

inputVar = 0
count = 0

inputVar = list(map(int, sys.stdin.readlines()))

for i in inputVar:
   if i % k == 0:
       count += 

'''
Key Concepts:
-sys.stdin() is a faster way to read input
-eval transforms something into an integer
-map applies a transformation to a specific input
-modolus = original input divided by first dividing
initial number by the modulus input, then multiplying
that result by the quotient and then subtract this result
from the original number
-multiple variables separated by a comma on the left side of 
an equation
'''
