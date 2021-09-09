def binary_search(sequence, target):
    first = 0
    last = len(sequence) - 1
    # found = False
    while first <= last and not False:
        mid = (first + last) // 2
        if sequence[mid] == target:
            return mid
        else:
            if target < sequence[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return None


# pybites


def _get_midpoint(start, stop):
    mid = (stop - start) / 2
    return 1 if mid == 0.5 else int(mid)


def binary_search(sequence, target, select=0, start=None, stop=None):
    if not start and not stop:
        start = 0
        stop = len(sequence) - 1
        select = _get_midpoint(start, stop)

    if sequence[select] == target:
        return select
    elif select == start == stop:
        return None

    start = select + 1 if sequence[select] < target else start
    stop = select if sequence[select] > target else stop
    change = _get_midpoint(start, stop)

    if change == 0 and sequence[start] == target:
        return start

    select += change if sequence[select] < target else change * -1
    return binary_search(sequence, target, select, start, stop)
