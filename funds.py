from itertools import combinations

IMPOSSIBLE = 'Mission impossible. No one can contribute.'

#kayode's

def max_fund(village):
    """Find a contiguous subarray with the largest sum."""
    # Hint: while iterating, you could save the best_sum collected so far
    # return total, starting, ending
    index_combination = combinations(range(len(village) + 1), 2)
    ret_list = []
    for i, j in index_combination:
        ret_list.append((sum(village[i:j]), i+1, j))
    ret_tuple = max(ret_list, key = lambda x: x[0])
    if ret_tuple[0] < 0: 
        print(IMPOSSIBLE)
        return (0,0,0)
    else:
        return ret_tuple


#pybites
def max_fund(village):
    """Find a contiguous subarray with the largest sum."""
    best_sum, current_sum = 0, 0
    best_start, best_end = 0, 0

    # 1. extreme case - all poor
    if all(n <= 0 for n in village):
        print(IMPOSSIBLE)
        return (0, 0, 0)

    # 2. mission is possible - start the trip now
    for current_end, x in enumerate(village):
        if current_sum <= 0:
            current_start = current_end
            current_sum = x
        else:
            current_sum += x
        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = current_end
    # index offset:  start + 1, end + 1
    return best_sum, best_start + 1, best_end + 1
