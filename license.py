bites = {6: 'PyBites Die Hard',
         7: 'Parsing dates from logs',
         9: 'Palindromes',
         10: 'Practice exceptions',
         11: 'Enrich a class with dunder methods',
         12: 'Write a user validation function',
         13: 'Convert dict in namedtuple/json',
         14: 'Generate a table of n sequences',
         15: 'Enumerate 2 sequences',
         16: 'Special PyBites date generator',
         17: 'Form teams from a group of friends',
         18: 'Find the most common word',
         19: 'Write a simple property',
         20: 'Write a context manager',
         21: 'Query a nested data structure'}
exclude_bites = {6, 10, 16, 18, 21}


def filter_bites(bites=bites, bites_done=exclude_bites):
    """return the bites dict with the exclude_bites filtered out"""
    return {numb:res for numd, res in bites.items(): if numb not in exclude_bites}

filter_bites()






import random, string

def gen_key( parts=4, chars_per_part = 8):
    password_characters = string.ascii_uppercase + string.digits
    password = []
    for x in range(parts):
        result_str = ''.join(random.choices(password_characters, k=chars_per_part))
        password.append(result_str)
        final_result= str('-'.join(password))
        
    return final_result
    

'''from secrets import choice
from string import ascii_uppercase, digits

ALPHABET = ascii_uppercase + digits
DASH = '-'


def gen_key(parts=4, chars_per_part=8):
    return DASH.join(''.join(choice(ALPHABET) for i in range(chars_per_part))
                     for _ in range(parts))'''