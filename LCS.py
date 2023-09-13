'''
Problem

LCS - Longest Common Substring
no tags 
A string is finite sequence of characters over a non-empty finite set Σ.

In this problem, Σ is the set of lowercase letters.

Substring, also called factor, is a consecutive sequence of characters occurrences at least once in a string.

Now your task is simple, for two given strings, find the length of the longest common substring of them.

Here common substring means a substring of two or more strings.

Input
The input contains exactly two lines, each line consists of no more than 250000 lowercase letters, representing a string.

Output
The length of the longest common substring. If such string doesn't exist, print "0" instead.

Example
Input:
alsdfkjfjkdsal
fdjskalajfkdsla

Output:
3
'''

import sys

MAXLEN = 250052
K = 26

class State:
    def __init__(self):
        self.length = 0
        self.link = 0
        self.next = [-1] * K

st = [State() for _ in range(MAXLEN*2-1)]
sz = 0
last = 0
A = [''] * MAXLEN
B = [''] * MAXLEN

def init():
    global sz
    st[0].link = -1
    st[0].next = [-1] * K
    sz += 1

def extend(c):
    global sz, last
    nlast = sz
    sz += 1
    st[nlast].length = st[last].length + 1
    st[nlast].next = [-1] * K
    p = last
    while p != -1 and st[p].next[c] == -1:
        st[p].next[c] = nlast
        p = st[p].link
    if p == -1:
        st[nlast].link = 0
    else:
        q = st[p].next[c]
        if st[p].length + 1 == st[q].length:
            st[nlast].link = q
        else:
            clone = sz
            sz += 1
            st[clone].length = st[p].length + 1
            st[clone].next = st[q].next.copy()
            st[clone].link = st[q].link
            while p != -1 and st[p].next[c] == q:
                st[p].next[c] = clone
                p = st[p].link
            st[q].link = st[nlast].link = clone
    last = nlast

def lcs(a, b):
    global last
    init()
    for i in range(len(a)):
        extend(ord(a[i]) - ord('a'))
    p = 0
    l = 0
    best = 0
    bestpos = 0
    for i in range(len(b)):
        if st[p].next[ord(b[i]) - ord('a')] == -1:
            while p != -1 and st[p].next[ord(b[i]) - ord('a')] == -1:
                p = st[p].link
            if p == -1:
                p = l = 0
                continue
            l = st[p].length
        p = st[p].next[ord(b[i]) - ord('a')]
        l += 1
        if l > best:
            best = l
            bestpos = i
    return best

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()
print(lcs(A, B))

'''
code development inspiration from cacophonix
'''
