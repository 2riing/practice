import sys
sys.stdin = open('input.txt')

n = int(input())
arr = list(map(int, input().split()))

A = len(arr) # 5
for i in range(A, 0, -1): # A 부터 0까지 (A는 포함 되고 0은 포함 안된다)
    print(arr[i-1], end= ' ')