from collections import deque

def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    test_str = deque(list(string))
    test_str.rotate(-n)
    ret = ''.join(test_str)
    return ret




#pybites
def rotate(string, n):
    return string[n:] + string[:n]

#string = 'bob and julian love pybites!'
rotate('hello', 2)
rotate('hello', -2)