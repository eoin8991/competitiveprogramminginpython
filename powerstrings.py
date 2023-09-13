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
