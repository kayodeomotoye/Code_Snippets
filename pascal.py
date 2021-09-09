from typing import List


def pascal(N: int) -> List[int]:
    """
    Return the Nth row of Pascal triangle
    """
    if N == 0: return []
    N = N - 1
    line = [1]

    for k in range(max(N ,0)):
        line.append(int(line[k]*(N-k)/(k+1)))
    return line


#pybites

from math import factorial


# Solution 1
def Pascal(N):
    rows = [0 for _ in range(N + 1)]
    rows[1] = 1

    for i in range(1, N + 1):
        for j in range(i, 0, -1):
            rows[j] += rows[j - 1]

    return rows[1:]


# ----------------------------
# Solution 2:  use math formula
def nCr(n, r):
    return factorial(n) // factorial(r) // factorial(n-r)


def pascal(N):
    return [nCr(N-1, i) for i in range(N)]

