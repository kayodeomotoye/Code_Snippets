from itertools import cycle
import string


def sequence_generator():
    new_list =[]
    for num, alphabet in enumerate(string.ascii_uppercase, 1):
        new_list.append(num)
        new_list.append(alphabet)
    yield from cycle(new_list)
    


#pybites

from itertools import cycle
from string import ascii_uppercase


def sequence_generator():
    numbers = cycle(range(1, len(ascii_uppercase) + 1))
    letters = cycle(ascii_uppercase)

    for number, letter in zip(numbers, letters):
        yield number
        yield letter