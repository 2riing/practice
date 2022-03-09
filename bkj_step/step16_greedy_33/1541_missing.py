import sys
sys.stdin = open('input.txt')

calculations = input()

plus_sign = 0
minus_sign = 0
nums = []
cnt = 0
temp = ''
for calculation in calculations: # +- sign의 수와 nums 배열 만들어주기
    if calculation == '+':
        nums.append(int(temp))
        temp = ''
        plus_sign += 1
    elif calculation == '-':
        nums.append(int(temp))
        temp = ''
        minus_sign += 1
    else:
        temp += calculation
nums.append(int(temp))
nums.sort() # 최소로 정렬해 줌

result_temp = nums[0]
if plus_sign > 0:
        for i in range(plus_sign): # 작은수부터 다 더해줌
            result_temp += nums[i+1]
if minus_sign > 0:
    result = nums[plus_sign+1] - result_temp
    for j in range(1, minus_sign):
        result -= nums[plus_sign+j+1]
    print(result)
else:
    print(result_temp)



