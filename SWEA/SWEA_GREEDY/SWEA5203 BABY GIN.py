import sys
sys.stdin = open('input.txt')

def Win(a, b):
    # payler 1 triplet
    if 3 in card_cntA:
        return 1
    # plyer 2 run
    elif a > 1 and card_cntA[a - 1] > 0 and card_cntA[a - 2] > 0:
        return 1
    elif a > 0 and a < 9 and card_cntA[a + 1] > 0 and card_cntA[a - 1] > 0:
        return 1
    elif a < 8 and card_cntA[a + 1] > 0 and card_cntA[a + 2] > 0:
        return 1
    # player 2 triplet
    elif 3 in card_cntB:
        return 2
    # player 2 run
    elif b > 1 and card_cntB[b - 1] > 0 and card_cntB[b - 2] > 0:
        return 2
    elif b > 0 and b < 9 and card_cntB[b + 1] > 0 and card_cntB[b - 1] > 0:
        return 2
    elif b < 8 and card_cntB[b + 1] > 0 and card_cntB[b + 2] > 0:
        return 2
# 기본 인풋
T = int(input())
for tc in range(1, T+1):
    case = list(map(int, input().split()))
    # pop으로 꺼내주려고 reverse
    case.reverse()
    a, b = 0, 0
    card_cntA, card_cntB = [0] * 10, [0] * 10
    results = []
    # Win함수를 들면서 result에 추가해줌
    for i in range(int(len(case)/2)):
        a = case.pop()
        b = case.pop()
        card_cntA[a] += 1
        card_cntB[b] += 1
        results.append(Win(a, b))
    # result 중에 가장 첫번째것 출력
    for result in results:
        if result != None:
            print(f'#{tc} {result}')
            break
    # 전부 None이면 0 출력
    else:
        print(f'#{tc} 0')



