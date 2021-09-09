import itertools
import os
from posix import NGROUPS_MAX
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DICT}',
    DICTIONARY
)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    word_perm = _get_permutations_draw(draw) 
    return [''.join(line).lower() for line in word_perm if ''.join(line).lower() in dictionary]
    

def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    draw_str = ''.join(draw)
    ret_list= []
    for num in range(len(draw_str)):
        res = itertools.permutations(draw_str, r=num)
        for i in res:
            ret_list.append(i)
    return ret_list

#pybites
def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    permutations = [''.join(word).lower()
                    for word in _get_permutations_draw(draw)]
    return set(permutations) & set(dictionary)


def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    for i in range(1, 8):
        yield from itertools.permutations(draw, i)
        
    