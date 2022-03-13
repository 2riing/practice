import sys
sys.stdin = open('input.txt')

S = input()
abc = list(range(97, 123))
bucket = [-1]*26

for i in range(len(S)):
    for j in range(len(abc)):
        if ord(S[i]) == abc[j]:
            if bucket[j] == -1:
                bucket[j] = i
print(*bucket)
