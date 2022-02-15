arr = [[3, 5, 4],
       [1, 1, 2],
       [1, 3, 9]]
y, x = map(int, input().split()) # 1 1 엔터

d_y = [-1, 1, 0, 0]
d_x = [0, 0, -1, 1]

for i in range(4):
    dy = y + d_y[i]
    dx = x + d_x[i]
    if 0<=dy<=3 and 0<=dx<=3:
        total += arr[dy][dx]

print(total)