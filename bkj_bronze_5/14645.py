import sys
sys.stdin = open('input.txt')

A, B = list(map(int,input().split()))
print(A+B)