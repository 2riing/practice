import sys
sys.stdin = open('input.txt')

R1, S = list(map(int, input().split()))
print(S*2-R1)