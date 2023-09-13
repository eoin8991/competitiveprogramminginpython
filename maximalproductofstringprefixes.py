'''
Problem

Find the maximal product of string prefixes.

A prefix of a string S is any leading contiguous part of S. For example, "c" and "cod" are prefixes of the string 
"codility". For simplicity, we require prefixes to be non-empty.

The product of prefix P of string S is the number of occurrences of P multiplied by the length of P. More precisely, 
if prefix P consists of K characters and P occurs exactly T times in S, then the product equals K * T.

For example, S = "abababa" has the following prefixes:

"a", whose product equals 1 * 4 = 4,
"ab", whose product equals 2 * 3 = 6,
"aba", whose product equals 3 * 3 = 9,
"abab", whose product equals 4 * 2 = 8,
"ababa", whose product equals 5 * 2 = 10,
"ababab", whose product equals 6 * 1 = 6,
"abababa", whose product equals 7 * 1 = 7.
The longest prefix is identical to the original string. The goal is to choose such a prefix as maximizes the value of 
the product. In above example the maximal product is 10.

In this problem we consider only strings that consist of lower-case English letters (a−z).

Write a function

def solution(S)

that, given a string S consisting of N characters, returns the maximal product of any prefix of the given string. If 
the product is greater than 1,000,000,000 the function should return 1,000,000,000.

For example, for a string:

S = "abababa" the function should return 10, as explained above,
S = "aaa" the function should return 4, as the product of the prefix "aa" is maximal.
Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..300,000];
string S is made only of lowercase letters (a−z).
'''

import numpy as np

MAX = 10050
RA = np.zeros(MAX, dtype=int)
tempRA = np.zeros(MAX, dtype=int)
SA = np.zeros(MAX, dtype=int)
tempSA = np.zeros(MAX, dtype=int)
C = np.zeros(MAX, dtype=int)
Phi = np.zeros(MAX, dtype=int)
PLCP = np.zeros(MAX, dtype=int)
LCP = np.zeros(MAX, dtype=int)
SCR = np.zeros(MAX, dtype=int)

def suffix_sort(n, k):
    C.fill(0)
    for i in range(n):
        C[i + k if i + k < n else 0] += 1
    sum = 0
    for i in range(max(256, n)):
        t = C[i]
        C[i] = sum
        sum += t
    for i in range(n):
        tempSA[C[SA[i] + k if SA[i] + k < n else 0]] = SA[i]
    SA[:] = tempSA[:]

def suffix_array(s):
    n = len(s)
    for i in range(n):
        RA[i] = ord(s[i]) - 1
    for i in range(n):
        SA[i] = i
    k = 1
    while k < n:
        suffix_sort(n, k)
        suffix_sort(n, 0)
        r = tempRA[SA[0]] = 0
        for i in range(1, n):
            s1 = SA[i]
            s2 = SA[i-1]
            equal = True
            equal &= RA[s1] == RA[s2]
            equal &= RA[s1+k] == RA[s2+k]
            tempRA[SA[i]] = r if equal else r + 1
        RA[:] = tempRA[:]
        k *= 2

def lcp(s):
    n = len(s)
    Phi[SA[0]] = -1
    for i in range(1, n):
        Phi[SA[i]] = SA[i-1]
    L = 0
    for i in range(n):
        if Phi[i] == -1:
            PLCP[i] = 0
            continue
        while s[i + L] == s[Phi[i] + L]:
            L += 1
        PLCP[i] = L
        L = max(L-1, 0)
    for i in range(1, n):
        LCP[i] = PLCP[SA[i]]

def score(s):
    SCR[s.size()-1] = 1
    sum = 1
    for i in range(s.size()-2, -1, -1):
        if LCP[i+1] < s.size()-SA[i]-1:
            sum = 1
        else:
            sum += 1
        SCR[i] = sum

s = "abababa"
s = s[::-1] + "."
suffix_array(s)
lcp(s)
score(s)
for i in range(len(s)):
    ns = s[SA[i]:len(s)-SA[i]-1]
    ns = ns[::-1]
    print(SCR[i], "*", len(ns), ns)

'''
code development inspiration from Juan Lopes
see also the bekkairi mansour solution
'''
