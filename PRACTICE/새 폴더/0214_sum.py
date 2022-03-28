arr = [[3,4,1],[4,5,1],[3,8,3]]

sum_=10

for i in range(0,3):
    sum_ += arr[i][2-i]

print(sum_)
