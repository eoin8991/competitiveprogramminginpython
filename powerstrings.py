'''
Problem

Given two strings 
a and 
b we define 
a⋅b to be their concatenation. For example, if 
a="abc" and 
b="def" then 
a⋅b="abcdef". If we think of concatenation as multiplication, exponentiation by a non-negative integer is defined in the normal way: 
a to the 
0 power
=
"" empty string and 

a to the
n+1 power
 =a⋅a to the
n power
 .

Input
The input consists of up to 
10
10 test cases. Each test case is a line of input containing 
s, a string of lower case letters (a-z). The length of 
s will be at least 
1 and will not exceed 
2000000 characters. A line containing a period follows the last test case.

Output
For each 
s you should print the largest 
n such that 

s=a to the
n power
  for some string 
a.

Sample 1
Input
abcd
aaaa
ababab

Output
1
4
3

'''

#Two solutions
#1 

import sys

def check(s, n):
    for i in range(n, len(s)):
        if s[i] != s[i-n]:
            return False
    return True

def main():
    s = input().strip()
    while s != ".":
        n = len(s)
        for i in range(1, n+1):
            if n % i == 0:
                if check(s, i):
                    print(n//i)
                    break
        s = input().strip()

if __name__ == "__main__":
    main()

'''
code development inspiration from mpfeifer1
'''

#2

from sys import stdin

def find_divisors(n):
	divisors = []
	maxi = int((n**(0.5)+1))
	for i in range(1, maxi+1):
		if n % i == 0:
			divisors.append(i)
			divisors.append(n//i)
	return sorted(list(set(divisors)))

line = stdin.readline().strip()
while line != ".":
	length = len(line)
	divisors = find_divisors(length)
	for n in divisors:
		if line[-n:]*(length//n) == line:
			ans = (length//n)
			break
	print(ans)
	line = stdin.readline().strip()

'''
code development credit from xCiaraG
'''

###the code does not seem to be printing the desired n, but it's possible
#this kattis question has evolved over time
