


N, M = map(int, input().split())

data_dict = {}

for _ in range(N):
    url, pw = map(str, input().split())
    data_dict[url] = pw

for _ in range(M):
    find = input()
    print(data_dict[find])








# M개의 줄에 걸쳐 주소가 한 줄에 한 개씩 입력된다. 