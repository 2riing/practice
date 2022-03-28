import sys
sys.stdin=open('input.txt')

# 기본 입력 및 변수 초기화
T = int(input())
for tc in range(1,T+1):
    N = int(input()) #카드의 장수
    numbers = list(map(int, input()))
    bucket = [0]*10
    max_num = 0
    max_idx = 0

    for number in numbers:
        bucket[number] += 1 # 0~9까지 해당하는 자리에 +1씩 더해줌

    for i in range(len(bucket)):
        if bucket[i] >= max_num: # bucket에 가장 많이 담긴 숫자를 인덱스로 찾아냄
            max_num = bucket[i]
            max_idx = i

    # 출력
    print(f'#{tc} {max_idx} {bucket[max_idx]}')