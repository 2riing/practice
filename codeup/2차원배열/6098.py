import sys
sys.stdin = open('input.txt')

home = []
for _ in range(10):
    home.append(list(map(int, input().split())))

def Go(row, col):
    if home[row][col] == 2 or (col == 9 and row == 9): # base case 지정
        home[row][col] = 9 # 내 위치에 9를 저장하고
        return # 함수를 끝낸다
    elif col + 1 < 9 and (home[row][col + 1] == 0 or home[row][col + 1] == 2):
        # 오른쪽으로 이동한 값의 인덱스가 9보다 작으면서
        # 오른쪽으로 이동한 값이 0 이라면
        # 오른쪽 이동해도 괜찮음
        home[row][col] = 9 # 현재 위치에 9를 저장한 다음
        Go(row, col+1) # x+1을 넘겨서 Go 함수 실행.
    elif row + 1 < 9 and (home[row + 1][col] == 0 or home[row + 1][col] == 2):
        # 아래로 이동한 값의 인덱스가 9보다 작으면서
        # 아래로 이동한 값이 0이라면
        # 아래로 이동해도 괜찮음
        home[row][col] = 9 # 현재 위치에 9를 저장한 다음
        Go(row+1, col) # y+1을 넘겨서 Go 함수 실행.
    else:
        home[row][col] = 9
        return
Go(1,1)

for i in range(len(home)):
    print(*home[i])


