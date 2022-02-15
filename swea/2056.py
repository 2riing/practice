import sys
sys.stdin = open('input.txt')

# 1,3,5,7,8,10,12 는 31일까지
# 4, 9,11는 30일 까지

mon_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mon_list = [1,2,3,4,5,6,7,8,9,10,11,12]

T = int(input())
for tc in range(1, T+1):
    cal = input()
    year = cal[0:4]
    mon = cal[4:6]
    day = cal[6:8]
    # print(year, mon, day)

    if int(year) > 0:
        if int(mon) in mon_list:
            if int(day) <= mon_day[int(mon)-1]:
                print(f'#{tc} {year}/{mon}/{day}')
            else :
                print(f'#{tc} -1')
        else:
            print(f'#{tc} -1')


