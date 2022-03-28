import sys
sys.stdin = open('input.txt')

A, I = list(map(int, input().split()))
print(A * (I - 1) + 1)