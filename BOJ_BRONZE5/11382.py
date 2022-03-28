import sys
sys.stdin = open('input.txt')

a, b, c = list(map(int,input().split()))
print(a+b+c)