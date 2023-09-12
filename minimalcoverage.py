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
