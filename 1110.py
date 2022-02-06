




# 2 + 6 = 08 = 68 => 
# 6 + 8 = 14 = 84 => 
# 8 + 4 = 12 = 42 =>
# 1 +  




N = input()
cnt = 0
num = N
while True:
    if len(num)==1:
        num = "0" + num 
        # num type str
    else:
        plus = int(num[0]) + int(num[-1]) 
        # 중간과정을 의미함 앞자리수 + 뒷자리수 
        # plus의 타입 : int
        num = num[-1] + str(plus)[-1]
        # 새로운 수를 저장함 str : num의 뒷자리 + plus뒷자리 
        cnt += 1
        if int(num) == int(N):
            print(cnt)
            break
    
