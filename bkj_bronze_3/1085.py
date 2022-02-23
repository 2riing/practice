import sys
sys.stdin=open('input.txt')

# 직사각형의 경계선 까지 가는 최솟값
x, y, w, h = list(map(int, input().split()))

# x축에서 a = x, b = w-x
# y축에서 c = y, d = h-y

min_list = [x, y, w-x, h-y]
print(min(min_list))