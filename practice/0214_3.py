arr = [[3,4,1],[4,5,1],[3,8,3]]

sum = 0
Max = int(-21e8)
for j in range(3):
    sum=0
    for i in range(3):
        sum+= arr[i][j]
    if Max < sum:
        Max=sum
print(Max)