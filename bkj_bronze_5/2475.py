import sys
sys.stdin = open('input.txt')

arr = list(map(int,input().split()))
total = 0
for i in range(len(arr)):
    total += arr[i] ** 2

print(total%10)