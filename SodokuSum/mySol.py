from itertools import permutations

ALL_VALUES = [1,2,3,4,5,6]
SUM = 14
SQUARES = 4


def findAllPermutations():
    lst = []
    for i in permutations(ALL_VALUES, SQUARES):
        if sum(i) == SUM:
            lst.append(sorted(i))

    return [t for t in (set(tuple(i) for i in lst))]

print(findAllPermutations())