import sys
sys.stdin = open('input.txt')

D, H, W = list(map(int, input().split()))

print(D, H, W)

print((D ** 2 / (H+W) *H)**0.5 )
print(D ** 2 / (H+W) *W )