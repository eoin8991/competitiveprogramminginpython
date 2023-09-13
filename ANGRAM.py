'''
Problem

ANGRAM - Anagram verifier
no tags 
An anagram is a rearrangement of the letters of an existing phrase to create a new phrase. For example, ananagram of 
"Tom Marvolo Riddle" is "I Am Lord Voldemort".

Given two phrases, answer whether they are anagrams. The phrases will be given in the lowercase letters a-z with spaces removed.

(Note: For this problem, every phrase is considered to be an anagram of itself.)

Input
The first line is an integer T (between 1 to 20, inclusive), which is the number of supposed anagram pairs to follow.

On the next T lines will be two sequences of lowercase letters. These are the two phrases. Neither will exceed 10000 characters.

Output
For each supposed anagram pair, print a line with "true" if they are anagrams and "false" otherwise.

Example
Input:
3
tommarvoloriddle iamlordvoldemort
aaa aba
iamaweakishspeller williamshakespeare

Output:
true
false
true
'''

#testing whether two strings are anagrams of each other is a common task

#https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/

'''
One example:
code development inspiration from proconjr
'''

def sort_array(array, length):
    for c in range(length):
        for d in range(length - c):
            if array[d] > array[d + 1]:
                temp = array[d]
                array[d] = array[d + 1]
                array[d + 1] = temp

a = input()
b = input()
l1 = len(a)
l2 = len(b)
if l1 != l2:
    print("Yes")
else:
    a = list(a)
    b = list(b)
    sort_array(a, l1)
    sort_array(b, l2)
    flag = True
    for i in range(l1):
        if a[i] != b[i]:
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")

  ###see also https://github.com/viraj071/SPOJ/blob/master/5872.%20Anagram/ANAG.cpp

'''
Key Concepts:
-using the sort function to determine if two strings are the same as each other
-how to insert a break into a function to cover one possible outcome
'''
