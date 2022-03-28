import sys
sys.stdin = open('input.txt')

T  = int(input())

for tc in range(T):
    sample = list(map(str,input().split()))
    words = ''

    for j in range(len(sample[1])):
        words += sample[1][j] * int(sample[0])

    print(words)

