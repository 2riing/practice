import sys
sys.stdin = open('input.txt')

arr = [int(input()) for _ in range(3)]
chk = [0]*10

result = 1
for a in arr:
    result *= a

for r in str(result):
    for i in range(len(chk)):
        if r == str(i):
            chk[i] += 1

for i in range(len(chk)):
    print(chk[i])
