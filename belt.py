import itertools
from collections import OrderedDict


scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()


def get_belt(user_score, scores=scores, belts=belts):
    score_dict=  OrderedDict(zip(scores, belts))
    if user_score in score_dict.keys(): user_belt= score_dict[user_score]
    elif user_score in range(10): user_belt = None
    elif user_score in range(11, 50): user_belt = 'white'
    elif user_score in range(51, 100): user_belt = 'yellow'
    elif user_score in range(101, 175): user_belt = 'orange'
    elif user_score in range(176, 250): user_belt = 'green'
    elif user_score in range(251, 400): user_belt = 'blue'
    elif user_score in range(401, 600): user_belt = 'brown'
    elif user_score in range(601, 800): user_belt = 'black'
    elif user_score in range(801, 1000): user_belt = 'paneled'
    elif user_score >= 1000: user_belt= 'red'

    return user_belt
   

    
    
#pybites

def get_belt(user_score):
    """new solution (see forum for old solution)"""
    for score, belt in zip(scores[::-1], belts[::-1]):
        if user_score >= score:
            return belt

   