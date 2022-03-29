import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 컨테이너수 N, 트럭수 M
    container, truck = deque(), deque()
    W = list(map(int, input().split())) # 컨테이너의 무게
    T = list(map(int, input().split())) # 트럭의 적재 용량
    W.sort(reverse=True)
    T.sort(reverse=True)
    for w in W:
        container.append(w)
    for t in T:
        truck.append(t)

    total = 0
    temp = truck[0]
    if container[0] <= temp:
        total += container.popleft()
        truck.popleft()
        temp = truck.popleft()
    while truck and container:
        if container[0] <= temp:
            total += container.popleft()
            temp = truck.popleft()
        else:
            container.popleft()

    print(f'#{tc} {total}')


