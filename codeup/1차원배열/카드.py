import sys
sys.stdin = open('input.txt')

N = int(input())
cards =[int(input()) for _ in range(N-1)]

bucket = [0] * N

for i in range(len(cards)):
    bucket[cards[i]-1] += 1
for j in range(len(bucket)):
    if bucket[j] == False:
        print(j+1)

