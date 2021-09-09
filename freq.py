#Kayode's code
from collections import Counter

def freq_digit(num: int) -> int:
    return int(Counter(str(num)).most_common(1)[0][0])




#Pybites' code
from collections import Counter


def freq_digit(num: int) -> int:
    cnt = Counter(str(num))
    top = int(cnt.most_common(1)[0][0])
    return top


if __name__ == '__main__':
    list_num = [1998, 2020, 12345, 177]
    for n in list_num:
        print(freq_digit(n))