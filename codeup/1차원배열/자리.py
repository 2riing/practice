import sys
sys.stdin = open('input.txt')

N, C = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

while len(arr) !=0:
    print(*arr[:C], end =' \n')
    arr = arr[C:]