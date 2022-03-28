
id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

report = str(set(report))
print(type(report))
print(list(map(str, str(report).split())))

def solution(id_list, report, k):
    answer = []

    #  각 유저가 받은 결과 메일 수를 담음
    return answer