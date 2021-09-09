from itertools import combinations
from itertools import permutations


def friends_teams(friends, team_size: int =2, order_does_matter: bool = False):
    if order_does_matter:
        func = permutations       
    else:
        func = combinations
    return func(friends, team_size)


