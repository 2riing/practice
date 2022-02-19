import sys
sys.stdin = open('input.txt')

N = int(input())
for i in range(0,N+1):
    print(f'{2**(i)}', end=' ')