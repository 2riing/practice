# Probelm 1 세로로 출력하기 
a = int(input())

for i in range(a):
    print(str(i+1))

print("---")

# 2 거꾸로 세로로 출력하기 

for i in range(a):
    print(str(a-i))

print("---")

# 3 n줄 덧셈 
# 1부터 num까지의 수를 도우 더한 값
total = 0
for i in range(a):
    total += i
print(total+a)
