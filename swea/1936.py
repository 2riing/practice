import sys
sys.stdin = open('input.txt')

# 가위 1 바위 2 보 3

A, B = list(map(int,input().split()))

if (A == 3 and B == 1):
    print('B')
elif (B == 3 and A ==1):
    print('A')
elif A>B:
    print('A')
else:
    print('B')