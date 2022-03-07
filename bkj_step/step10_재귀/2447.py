import sys
sys.stdin = open('input.txt')

N = int(input())

def fac(num):
    if num > 1:
        return num * fac(num-1) 
    elif num == 1 or num ==0 :
        return 1

print(fac(N))
