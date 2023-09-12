'''
CISTFILL - Fill the Cisterns
#binary-search
During the next century certain regions on earth will experience severe water shortages. 
The old town of Uqbar has already started to prepare itself for the worst. Recently they created a network 
of pipes connecting the cisterns that distribute water in each neighbourhood, making it easier to fill them 
at once from a single source of water. But in case of water shortage the cisterns above a certain level will 
be empty since the water will flow to the cisterns below.

Example of cistern arrangement
You have been asked to write a program to compute the level to which cisterns will be filled with a certain 
volume of water, given the dimensions and position of each cistern. To simplify we will neglect the volume of water in the pipes.

Task
Write a program that:

-reads the description of cisterns and the volume of water,
-computes the level to which the cisterns will be filled with the given amount of water,
-writes the result.

Input
The first line of the input contains the number of data sets k, 1 <= k <= 30. The data sets follow.

The first line of each data set contains one integer n, the number of cisterns, 1 <= n <= 50000. Each of the following 
n lines consists of 4 nonnegative integers, separated by single spaces: b, h, w, d - the base level of the cistern, its 
height, width and depth in meters, respectively. The integers satisfy 0 <= b <= 106 and 1 <= h*w*d <= 40000. The last line 
of the data set contains an integer V - the volume of water in cubic meters to be injected into the network. Integer V satisfies 1 <= V <= 2*109.

Output
The output should consist of exactly d lines, one line for each data set. Line i, 1 <= i <= d, should contain the level that the water will reach, 
in meters, rounded to two fractional digits, or the word "OVERFLOW" (without quotes), if the volume of water exceeds the total capacity of the cisterns.

Example
Sample input:
3 
2 
0 1 1 1 
2 1 1 1 
1 
4 
11 7 5 1 
15 6 2 2 
5 8 5 1 
19 4 8 1 
132 
4 
11 7 5 1 
15 6 2 2 
5 8 5 1 
19 4 8 1 
78 

Sample output:
1.00 
OVERFLOW 
17.00 
'''

import math

n = 0
a = [[0 for _ in range(3)] for _ in range(50001)]
y = 0
v = 0
filled = 0.0

def check(mid):
    global filled
    x = 0
    filled = 0
    for i in range(n):
        x = a[i][0] + a[i][1]
        if mid >= x:
            filled += a[i][2]
        elif mid < x and mid > a[i][0]:
            filled += (mid - a[i][0]) * a[i][2] / a[i][1]
    if filled >= v:
        return 0
    return 1

def binarysearch():
    start = 0.0
    end = 1040000.0
    for i in range(100):
        mid = (start + end) / 2.0
        if check(mid) == 1:
            start = mid
        else:
            end = mid
    return start

k = int(input())
while k > 0:
    v = 0
    total = 0.0
    n = int(input())
    for i in range(n):
        summ = 1
        for j in range(4):
            y = int(input())
            if j == 1:
                a[i][j] = y
            if j == 0:
                a[i][j] = y
            else:
                summ *= y
        a[i][2] = summ
        total += summ
    v = int(input())
    if total < v:
        print("OVERFLOW")
    else:
        print("{:.2f}".format(binarysearch()))
    k -= 1

'''
code development inspiration from viraj071
'''

'''
Key concepts:
-using "{.2f}".format() to print a result to two decimal places
'''
