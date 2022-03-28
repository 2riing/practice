import sys
sys.stdin = open('input.txt')

n = int(input())
arr = list(map(int, input().split()))
print(*arr)
temp = arr[0]
for j in range(len(arr)-1):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[-1] = temp
    print(*arr)


    # 1일경우 arr[0]  = arr[1]
    # 2일경우 arr[1] = arr[2]