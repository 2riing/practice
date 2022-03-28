import sys
sys.stdin=open('input.txt')

N = int(input(),8)
print(bin(N)[2:])