import sys
sys.stdin = open('input.txt')

abcds = list(input())
print(abcds)
for abcd in abcds:
    print(f'{ord(abcd)-64} ',end='')
