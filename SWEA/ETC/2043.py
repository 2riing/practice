import sys
sys.stdin = open('input.txt')



K, P = list(map(int, input().split()))
print(K-P+1)