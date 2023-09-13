'''
Problem

Here's the UVA online judge version of the problem:

https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=612

You, as a member of a development team for a new spell checking program, are to write a module
that will check the correctness of given words using a known dictionary of all correct words in all their
forms.

If the word is absent in the dictionary then it can be replaced by correct words (from the dictionary)
that can be obtained by one of the following operations:
• deleting of one letter from the word;
• replacing of one letter in the word with an arbitrary letter;
• inserting of one arbitrary letter into the word.

Your task is to write the program that will find all possible replacements from the dictionary for
every given word.

Input
The first line of the input is an integer N, then a blank line followed by N datasets. There is a blank
line between datasets.

The first part of each dataset contains all words from the dictionary. Each word occupies its own
line. This part is finished by the single character ‘#’ on a separate line. All words are different. There
will be at most 10000 words in the dictionary.

The next part of the dataset contains all words that are to be checked. Each word occupies its own
line. This part is also finished by the single character ‘#’ on a separate line. There will be at most 50
words that are to be checked.

All words in the input file (words from the dictionary and words to be checked) consist only of small
alphabetic characters and each one contains 15 characters at most.

Output
For each dataset, write exactly one line for every checked word in the order of their appearance in the
second part of the input. If the word is correct (i.e. it exists in the dictionary) write the message:
‘< checkedword > is correct’. If the word is not correct then write this word first, then write the
character ‘:’ (colon), and after a single space write all its possible replacements, separated by spaces.
The replacements should be written in the order of their appearance in the dictionary (in the first part
of the input). If there are no replacements for this word then the line feed should immediately follow
the colon.

Print a blank line between datasets.

Sample Input
1
i
is
has
have
be
my
more
contest
me
too
if
award
#
me
aware
m
contest
hav
oo
or
i
fi
mre
#
Sample Output
me is correct
aware: award
m: i my me
contest is correct
hav: has have
oo: too
or:
i is correct
fi: i
mre: more me
'''

import math

MAXN = 10005
st = [0] * 1000
dic = [''] * MAXN
wd = 0
ind = 0

def in_del(bb, ss):
    p = 0
    d = 0
    for i in range(len(ss)):
        f = 1
        for j in range(p, len(bb)):
            if ss[i] == bb[j]:
                f = 0
                p = j + 1
                break
        if f:
            return 0
    return 1

def Rep(bb, ss):
    d = 0
    for i in range(len(bb)):
        if bb[i] != ss[i]:
            d += 1
        if d > 1:
            return 0
    return 1

def Cal(ss):
    global ind
    l1 = len(ss)
    ind = 0
    for i in range(wd):
        l2 = len(dic[i])
        if abs(l1 - l2) > 1:
            continue
        if ss == dic[i]:
            print(ss, "is correct")
            return
        if l1 == l2 and Rep(ss, dic[i]):
            st[ind] = i
            ind += 1
        if l1 > l2 and in_del(ss, dic[i]):
            st[ind] = i
            ind += 1
        if l1 < l2 and in_del(dic[i], ss):
            st[ind] = i
            ind += 1
    print(ss, end=":")
    for i in range(ind):
        print(" ", dic[st[i]], end="")
    print()

kase = int(input())

while kase > 0:
    wd = 0
    while True:
        dic[wd] = input()
        if dic[wd] == "#":
            break
        wd += 1
    while True:
        temp = input()
        if temp == "#":
            break
        Cal(temp)
    if kase > 1:
        print()
    kase -= 1

'''
code development inspiration from limon2009
'''
