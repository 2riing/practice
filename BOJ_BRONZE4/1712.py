import sys
sys.stdin = open('input.txt')

# A: 고정비용
# B: 가변비용
# C: 노트북 가격
A, B, C = map(int, input().split())

def Find(A, B, C):
    i = A//C
    max = 2100000000//10
    for _ in range(max):
        if C < B:
            return -1
        elif A + (B * i) <= C * i:
            return i
        else:
            i += 1
    return -1

print(Find(A, B, C))
