'''
Problem available at 
https://github.com/google/coding-competitions-archive/blob/main/codejam/2008/round_1a/minimum_scalar_product/statement.pdf
'''

import sys

def cmp(a, b):
    return a > b

def main():
    t = int(input())
    kase = 0
    for _ in range(t):
        n = int(input())
        v1 = list(map(int, input().split()))
        v2 = list(map(int, input().split()))
        v1.sort()
        v2.sort(reverse=True)
        ret = 0
        for i in range(n):
            ret += v1[i] * v2[i]
        print("Case #{}: {}".format(kase+1, ret))
        kase += 1

if __name__ == "__main__":
    main()

'''
code credit inspiration from WArobot 
'''

'''
Key concepts:
-defining a function simply as a return with a condition, it returns True if the condition is true, 
and false if the condition is false
-sort() defaults to ranking in ascending order, and the reverse is descending order
-use "{}" with format() to fill in blank spaces
'''
