numbers =  [1, 2, 3]
N = len(numbers)

def perm(idx):
    if idx == N:
        print(*numbers)
        return
    for j in range(idx, N):
        numbers[idx] , numbers[j] = numbers[j], numbers[idx]
        perm(idx+1)
        numbers[idx] , numbers[j] = numbers[j], numbers[idx]
perm(0)
debug = 1