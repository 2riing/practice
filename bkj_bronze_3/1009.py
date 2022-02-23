import sys
sys.stdin=open('input.txt')

T = int(input())
for _ in range(T):
    a, b = list(map(int, input().split()))
    print((a**b)%10)

