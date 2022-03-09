import sys
sys.stdin = open('input.txt')

N = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))[:-1]
min_price = min(prices)
remain = sum(distances)


def CalculatePay(remain):
    pay = 0
    for i in range(len(distances)):
        if prices[i] == min_price:
            pay += min_price * remain
            return pay
        else:
            pay += prices[i] * distances[i]
            remain -= distances[i]
    return pay

print(CalculatePay(remain))