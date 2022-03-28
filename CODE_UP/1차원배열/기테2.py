import sys
sys.stdin = open('input.txt')

N = int(input())
num_list = list(map(int, input().split()))

M = int(input())
Q = list(map(int, input().split()))

for i in range(M):
    if Q[i] in num_list:
        print(1, end=' ')
    else:
        print(0, end=' ')