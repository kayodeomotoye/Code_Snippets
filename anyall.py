import string
import re

VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    if re.match('^[aeiou]*$', input_str.lower()):
        return True
        
    else:
        return False
            


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    for i in PYTHON:
        if i in input_str.lower():
            return True


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    for i in input_str:
        if i in string.digits:
            return True