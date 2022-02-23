

charge = 1683
cnt = 0
coins = [500,100,50,10]

for coin in coins:
    cnt += charge // coin
    charge = charge % coin

print(cnt)