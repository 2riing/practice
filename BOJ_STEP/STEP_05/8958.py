import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    ox = list(input())
    cnt = 0
    total = 0
    for i in range(len(ox)):
        if ox[i] == 'O':
            cnt += 1
        else:
            total += (cnt*(cnt+1))/2
            cnt = 0
    total += (cnt * (cnt + 1)) / 2
    print(round(total))
