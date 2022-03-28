import sys
sys.stdin = open('input.txt')

arr = input()
cnt1 = 0
cnt2 = 0
for a in arr:
    if a =='(':
        cnt1 += 1
    else:
        cnt2 += 1
print(cnt1 , cnt2)
