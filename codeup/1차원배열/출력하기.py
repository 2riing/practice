import sys
sys.stdin = open('input.txt')

words = input().split()
word = ''
for i in range(len(words)):
    word += words[i]
print(word)