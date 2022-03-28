import sys
from collections import deque
sys.stdin = open('input.txt')

N = int(input())
tree_parent = [0]*(N+1)
visited = [1]*(N+1) ; visited[0],visited[1] = 0,0
inputs = []
for _ in range(N-1):
    inputs.append(list(map(int, input().split())))
print(visited)


def FindParent(parent):

    global visited
    global inputs
    global tree_parent


    if sum(visited) == 0:
        return
    else:
        for j in range(2):
            for i in range(len(inputs)):
                # 앞줄검사 뒤-자식 앞-부모
                if  visited[inputs[i][1]] and inputs[i][j] == parent: # 뒤에있는 자식을 방문한 적이 없고, 지금 부모가 앞줄일 때
                    parent = inputs[i][1]  # 부모를 자식으로 바꿔줌
                    tree_parent[parent] = inputs[i][0] # 자식의 parent를 넣어줌
                    visited[parent] = 0 # 지나갔다고 체크
                # 뒷줄검사 앞-부모 뒤-자식
                elif visited[inputs[i][0]] and inputs[i][j] == parent:
                    parent = inputs[i][0]  # 부모를 자식으로 바꿔줌
                    tree_parent[parent] = inputs[i][1] # 자식의 parent를 넣어줌
                    visited[parent] = 0 # 지나갔다고 체크
            else:
                for k in range(len(visited)):
                    if visited[k] != 0:
                        parent = k
                        return FindParent(parent)


FindParent(1)
print(tree_parent)
print(visited)


