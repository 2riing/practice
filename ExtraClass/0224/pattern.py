map = [["A","B","G","K"],["T","T","A","B"],["A","C","C","D"]]
input = [list(input()) for _ in range(2)]
cnt = 0
for i in range(2):
    for j in range(3):
        if map[i][j] == input[0][0]:
            if map[i][j+1] == input[0][1]:
                if map[i+1][j] == input[1][0]:
                    if map[i+1][j+1] == input[1][1]:
                        cnt += 1
print(cnt)