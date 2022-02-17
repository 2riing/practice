# 9개의 서로 다른 자연수
# 이중 최대 값을 찾고 인덱스 받아 오기


N = []
for i in range(9):
    N.append(int(input()))
print(max(N))
print(N.index(max(N))+1)



