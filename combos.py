from itertools import combinations


def find_number_pairs(numbers, N=10):
    combination = combinations(numbers, 2)
    return [pair for pair in combination if sum(pair)== N]


#pybites

def find_number_pairs(numbers, N=10):
    return [(i, j) for i, j in combinations(numbers, 2)
            if i + j == N]
    


