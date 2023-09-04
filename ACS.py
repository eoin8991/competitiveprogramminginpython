'''
Problem

ACS - A concrete simulation

You are given a matrix M of type 1234x5678. It is initially filled with integers 1...1234x5678 
in row major order. Your task is to process a list of commands manipulating M. There are 4 types of commands:

"R x y" swap the x-th and y-th row of M;
"C x y" swap the x-th and y-th column of M;
"Q x y" write out M(x,y);
"W z" write out x and y where z=M(x,y).

Input
A list of valid commands. Input terminated by EOF.

Output
For each "Q x y" write out one line with the current value of M(x,y), for each "W z" write out 
one line with the value of x and y (interpreted as above) separated by a space.

Input:
R 1 2
Q 1 1
Q 2 1
W 1
W 5679
C 1 2
Q 1 1
Q 2 1
W 1
W 5679

Output:
5679
1
2 1
1 1
5680
2
2 2
1 2
'''

import sys

def main():
    r = [0] * 1235
    c = [0] * 5679
    revr = [0] * 1235
    revc = [0] * 5679

    for i in range(1, 1235):
        r[i] = i
        revr[i] = i

    for i in range(1, 5679):
        c[i] = i
        revc[i] = i

    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break

        op = line[0]
        if op == 'R':
            x, y = map(int, line[2:].split())
            r1 = r[x]
            r2 = r[y]
            r[x] = r2
            revr[r2] = x
            r[y] = r1
            revr[r1] = y
        elif op == 'C':
            x, y = map(int, line[2:].split())
            c1 = c[x]
            c2 = c[y]
            c[x] = c2
            revc[c2] = x
            c[y] = c1
            revc[c1] = y
        elif op == 'Q':
            x, y = map(int, line[2:].split())
            print((r[x] - 1) * 5678 + c[y])
        else:
            z = int(line[2:])
            z -= 1
            x = z // 5678
            y = z % 5678
            print(revr[x + 1], revc[y + 1])

if __name__ == '__main__':
    main()

'''
code guidance credit to marioyc
'''

'''
Key Concepts:
-Use while: True to repeat a function indefinitely until "if not" and "break"
-use elif repeatedly, then else at the end
'''
