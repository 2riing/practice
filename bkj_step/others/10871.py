



N, X = map(int, input().split())


# 수열 A를 이루는 정수 N개가 주어진다. 
A = list(map(int, input().split()))


# X보다 작은 수를 입력받은 순서대로 공백으로 구해서 출력한다.
for i in range (N):
    if A[i] < X:
        print(A[i], end=' ')
# 만약에 A[]가 X보다 작다면
# 공백으로 구분해서 A[0] + A[i] + A...





# 짜증나는 문제 - N개를 받아오라고 했는데, N개를 안받아도 채점이 된다. 
# 이해 안됨
