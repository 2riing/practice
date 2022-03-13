from itertools import permutations
numbers = [1, 2, 3, 4]

#numbers P4
for perm in permutations(numbers):
    print(perm)

# numbers P n
for perm in permutations(numbers, 3):
    print(perm)