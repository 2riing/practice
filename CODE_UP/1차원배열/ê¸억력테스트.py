import sys
sys.stdin = open('input.txt')

nums = list(map(int, input().split()))
k = int(input())

for i in range(len(nums)):
    if i == k-1:
        print(nums[i])
        break

