import sys
sys.stdin = open('input.txt')

n = int(input())
print(bin(n)[2:])