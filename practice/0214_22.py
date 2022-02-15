arr=[3,6,5,8,5,3,5,8,5,3,3,1,1,3]
pattern=[3,5,8,4]


def isPattern(index):
    for i in range(4):
        if pattern[i] != arr[i]:
            return