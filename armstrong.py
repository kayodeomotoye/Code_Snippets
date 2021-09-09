def is_armstrong(n: int) -> bool:
    str_num = str(n)
    len_num = list(enumerate(str_num, 1))
    total_num = 0
    for order, num in len_num:
        total_num += int(num) ** len(str_num)
    if total_num == n:
        return True
    else:
        return False




#pybites

def is_armstrong(n: int) -> bool:
    size = len(str(n))  # how many digits: size
    snum = str(n)
    total = sum(
        map(lambda x: x**size, map(int, snum))
    )

    return n == total

    # or as a one-liner
    # return n == sum(map(powered, map(int, snum)))