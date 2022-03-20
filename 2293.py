import sys
sys.stdin = open('input.txt')
import itertools
import psutil

def memory_usage():
    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2 ** 20 # Bytes to MB
    return f"{rss: 10.1f} MB"

n, k = map(int, input().split())
worth = [int(input()) for _ in range(n)]

# subsets = [[]]
# cnt = 0
# for i in range(1, len(worth)+k):
#
#     subsets = list(map(sum, list(itertools.combinations_with_replacement(worth, i))))
#     # print(subsets)
#     if subsets[0] > k:
#         break
#     else:
#         for j in subsets:
#             cnt_temp = 0
#             if j == k:
#                 cnt += 1
#
# print(cnt)


subsets = list(itertools.combinations_with_replacement(worth, 1))
print(memory_usage())


