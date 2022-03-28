import sys
sys.stdin = open('input.txt')

arr = [int(input())%42 for _ in range(10)]
chk = [0]*42

for a in arr:
    chk[a] += 1

cnt = 0
for c in range(len(chk)):
    if chk[c] >= 1:
        cnt += 1
print(cnt)
