'''
Problem

LPS - Longest Palindromic Substring
no tags 
A palindrome is a string that is the same as its reverse. Example "malayalam", "dad", 
"appa" etc. In this problem you are asked to find the length of the longest contiguous substring of a given string, which is a palindrome.

Input
The first line consists of a single integer N, the no. of characters in the string. 1 <= N <= 100000.

Second line is a string with N characters, where the characters are always lowercase English alphabets, i.e. 'a' to 'z'.

Output
A single line with an integer representing the length of longest palindromic substring.

Example
Input:
5
ababa

Output:
5
'''

import sys

p = 10007
MAXN = 100000

def hash(idx, length):
    return H[idx+length-1]-H[idx-1]*P[length]

def r_hash(idx, length):
    return r_H[idx+length-1]-r_H[idx-1]*P[length]

def odd_palin(idx):
    r_idx = limit-idx-1
    lo = 1
    hi = min(idx, r_idx)+1
    if hi == 1:
        return 0
    
    while lo < hi:
        mid = lo + (hi-lo)//2
        if hash(idx, mid+1) == r_hash(r_idx, mid+1):
            lo = mid+1
        else:
            hi = mid
    return lo-1

def even_palin(idx):
    r_idx = limit-idx
    lo = 1
    hi = min(idx-1, r_idx-1)+1
    if hi < lo:
        return 0
    
    while lo < hi:
        mid = lo + (hi-lo)//2
        if hash(idx, mid+1) == r_hash(r_idx, mid+1):
            lo = mid+1
        else:
            hi = mid
    return lo-1

limit = int(input())
word = input()

P = [0] * MAXN
H = [0] * MAXN
r_H = [0] * MAXN

P[0] = 1
H[0] = ord(word[0])
r_H[0] = ord(word[limit-1])

for i in range(1, limit):
    P[i] = P[i-1]*p
    H[i] = H[i-1]*p+ord(word[i])
    r_H[i] = r_H[i-1]*p+ord(word[limit-i-1])

maxpalin = 1

for i in range(1, limit):
    lpalin = odd_palin(i)*2+1
    if lpalin > maxpalin:
        maxpalin = lpalin
    if word[i] == word[i-1]:
        lpalin = even_palin(i)*2+2
        if lpalin > maxpalin:
            maxpalin = lpalin

print(maxpalin)

'''
code development inspiration from vfonic
'''
