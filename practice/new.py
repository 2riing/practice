

def fibo(n):
    global memo
    if n>=2 and len(memo) <= n:
        memo.append(fibo(n-1) + fibo(n-2))
        print(memo)
    return memo[n]
memo = [0,1]


print(fibo(3))

debug = 1