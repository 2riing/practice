
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# a, b, c, d = [int(input()) for _ in range(4)]
# total = a+ b+ c+ d
# print(total // 60)
# print(total % 60)

try:
    while 1:
        a = input()
except:
    exit()

print(a)
