'''
Encrpytion 

Marko is going to write a secret letter to a friend. He thought it is better to encrypt letter 
so that no other person can read it. After long thought he came up with an encryption scheme 
which was lame but he thought it will work anyways.

To encrypt a text he first wrote two infinite strings of characters first string consists only 
of vowels and second string consists of consonants only.

aeiouaeiouaeiouaeiouaeiou....................
bcdfghjklmnpqrstvwxyzbcdfghjklmnpqrstvwxyz...
 
Following is the scheme for encryption :

let c be any character to be encrypted.
let k be the count of number of times c character occurred in text to be encrypted until now.
first find which of two infinite string contains that character.
then look for kth occurrence of that character in that string.
replace character c by corresponding character in second string.
For example, encrypted text of "baax" will be "abho".

Input

First line of input will contains t, number of test cases. Then t test case follows each test 
case in a line. Each test case will be a string of small Latin alphabets. Length of string will be less than 5*10^4

Output

For each test case print encrypted text.

Sample :

Input:

2
baax
aaa

Output:

abho
bhn
'''

import sys

def main():
    t = int(input())
    for _ in range(t):
        cnt = [0] * 26
        s = input().strip()
        for c in s:
            cnt[ord(c) - ord('a')] += 1
            if c in ['a', 'e', 'i', 'o', 'u']:
                pos = ['a', 'e', 'i', 'o', 'u'].index(c)
                sys.stdout.write(['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 
                                  's', 't', 'v', 'w', 'x', 'y', 'z'][((cnt[ord(c) - ord('a')] - 1) * 5 + pos) % 21])
            else:
                pos = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'].index(c)
                sys.stdout.write(['a', 'e', 'i', 'o', 'u'][((cnt[ord(c) - ord('a')] - 1) * 21 + pos) % 5])
        sys.stdout.write('\n')

if __name__ == "__main__":
    main()

'''
Key concepts: 
-define a function named main()
-use __name__ == "__main__" to check if main() is initialized 
-sys.stdout.write() to write a result and you can define a set of inputs within br [] and put another [] next to it
to mathematically iniciate the index number
-sys.stdout.write('\n') to write the full result
'''

'''
source guidance credit to neeraj08
'''
