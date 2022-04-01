import sys
sys.stdin = open('input.txt')
from collections import deque

def BFS() -> int:
    q = deque()
    cnt = 0
    q.append((N, cnt))
    visited = set()
    visited.add(N)
    while q:
        v, cnt = q.popleft()
        for i in range(4):
            nv = [v + 1, v - 1, v * 2, v - 10]
            if 1 <= nv[i] <= 1000000 and nv[i] not in visited:
                visited.add(nv[i])
                q.append((nv[i], cnt + 1))
                if v == M:
                    return cnt
    return 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 현재 숫자, 도달해야하는 숫자
    cnt2 = BFS()
    print(f'#{tc} {cnt2}')
