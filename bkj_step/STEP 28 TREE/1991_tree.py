import sys
sys.stdin = open('input.txt')

N = int(input())
tree =  [list(input().split()) for _ in range(N)]
print(tree)
node_list = [0]*26 # A는 아스키코드 65번 부터
node = 0 # 트리의 노드는 i, 숫자 입니다.

def ChangeNum(word):
    result = ord(word)-65
    return result
def ChangeChr(num):
    result = chr(num+65)
    return result



# 전위순회
def pre_order(node):
    p = tree[node][0]
    print(p, end='')
    left_node = num_node()[node][1]
    right_node = ord(tree[node][2])-65
    pre_order(left)
    pre_order(right)

# # 중위순회
# def in_order(node):
#     p = tree[node][0]
#     in_order(1)
#     print(p)
#     in_order(2)
#
# # 후위순회
# def post_order(node):
#     p = tree[node][0]
#     post_order(1)
#     post_order(2)
#     print(p)
#
#
#
# pre_order(node)
# in_order(node)
# post_order(node)
