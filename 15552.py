

import sys

T = int(sys.stdin.readline())

total = 0 
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B) 