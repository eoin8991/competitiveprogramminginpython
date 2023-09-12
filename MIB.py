'''
Problem Statement

MIB - Spelling Lists
#sorting
J, of the Men In Black,  has been learning an alien language and has has a spelling test tomorrow.  
J, however, is bored of studying the nonsensical (and often unpronouncable) words.

Instead, he is seeing how many ways he can reorder his spelling list.  After making all possible 
permutations of word on his list, he sorts the rearranged lists lexiographically (by the first word, 
then the second...).  After the sort, in what position, with  the lexiographically first list being 
in position 1, is his original spelling list?

Input
The first line is the number of spelling lists (no more than 10).

For each spelling list, a line with the number of words (no more than 1000) is given, followed by 
the original list on the next line.

All words within a spelling list are unique.  Each word is composed of the letters a-z, is fewer 
than 100 characters, and is followed by a single space.

Output
On separate lines, give the positions of the original lists.

Example
Input:
4
4
a b c d 
4
d c b a 
1
mrsmith 
6
a aaaaaa aaaaa aaaa b bb 

Output:
1
24
1
55

'''
