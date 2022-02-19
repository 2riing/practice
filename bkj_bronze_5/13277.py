import sys
sys.stdin = open('input.txt')

a, b = list(map(int, input().split()))
print(a*b)