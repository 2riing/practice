import sys
sys.stdin = open('input.txt')

C = int(input())

for c in range(C):
    grade = list(map(int, input().split()))
    stu_num = grade[0]
    avg_grade = round((sum(grade)-stu_num)/stu_num,3)


    over_avg = 0
    for i in range(1, stu_num+1):
        if grade[i] > avg_grade:
            over_avg += 1

    print(f'{format(over_avg/grade[0]*100,".3f")}%')


