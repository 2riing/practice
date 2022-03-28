import sys
sys.stdin = open('input.txt')

dice = list(map(int, input().split()))
# 3개가 모두 같을 떄
if dice[0] == dice[1]:
    if dice[0] == dice[2]:
        prize = 10000 + dice[0]*1000
    else: # 2개인데 0,1 같을 때
        prize = 1000 + dice[0]*100
elif dice[0] == dice[2]:
    prize = 1000 + dice[0] * 100
elif dice[1] == dice[2]:
    prize = 1000 + dice[1] * 100
else:
    prize = max(dice) * 100

print(prize)