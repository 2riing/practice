import sys
sys.stdin = open('input.txt')

n = int(input())
k = list(map(int, input().split()))

def Compare(a, b):
    if a == b:
        result = '='
        return result
    elif a > b:
        result = '>'
        return result
    else:
        result = '<'
        return result



for i in range(n):
    total = []
    for j in range(n):
        if i != j:
            total.append(Compare(k[i], k[j]))
    print(f'{i+1}: {" ".join(total)}')
