import sys
sys.stdin = open('input.txt')


N = int(input())
arr = list(map(int, input().split()))


for i in range(1, len(arr)):
    for j in range(0, len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j+1], arr[j] = arr[j] , arr[j+1]

mid = round((N+1) / 2 -1)

print(f'{arr[mid]}')
