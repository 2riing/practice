import sys
sys.stdin = open('input.txt')

n = int(input())
student = [list(map(str, input().split())) for _ in range(n)]
grade = []

for i in range(n):
    grade.append(student[i][1])

grade = sorted(list(map(int, grade)))

for i in range(n):
    if int(student[i][1]) == grade[-3]:
        print(student[i][0])

