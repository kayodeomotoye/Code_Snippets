from collections import Counter
import os
from urllib.request import urlretrieve

from dateutil.parser import parse, parser

commits = os.path.join(os.getenv("TMP", "/tmp"), 'commits')
urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


def get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    with open(commits, 'r') as kyle:
        Current_Dict = {}
        for line in kyle.readlines():
            #print(line)
            res = parse(line.split()[5] +' '+ line.split()[2])
            res_key = YEAR_MONTH.format(y=res.year, m=res.month)
            res_value1= int(line.split()[11]) 
            try:
                res_value2 = int(line.split()[13])
            except IndexError:
                res_value2 = 0
            res_value = res_value1 + res_value2
            if not res_key in Current_Dict.keys():
                Current_Dict[res_key] = res_value
            else:
                Current_Dict[res_key] = Current_Dict[res_key] + res_value
    
    if year is None:
        new_min = min(Current_Dict.values())
        new_max= max(Current_Dict.values())
        for k, v in Current_Dict.items():
            if v == new_max: mam = k
            if v == new_min: lam = k
        
        return lam, mam
    else:
        res_dict = {k: v for k,v in Current_Dict.items() if str(year) in k}    
        new_min = min(res_dict.values())
        new_max= max(res_dict.values())
        for k, v in res_dict.items():
            if v == new_max: mam = k
            if v == new_min: lam = k

        return lam, mam




get_min_max_amount_of_commits()

#nhj= parse('2019 Mar')
#nkj = YEAR_MONTH.format(y=nhj.year, m=nhj.month) 
     
      



#pybites

from collections import Counter
import os
from urllib.request import urlretrieve

from dateutil.parser import parse

commits = os.path.join(os.getenv("TMP", "/tmp"), 'commits')
urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


def _get_int(ins_del_str):
    return int(ins_del_str.split()[0])


def get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    res = Counter()
    with open(commits) as f:
        for line in f.readlines():
            date, stats = line.split('|')
            dt = parse(date.replace('Date:', '').strip())

            if year and dt.year != year:
                continue

            mods = stats.split(', ')
            if len(mods) == 3:
                _, inserts, deletes = mods
            else:
                # in this case we have only inserts or deletes
                if 'insert' in mods[1]:
                    _, inserts = mods
                    deletes = '0 deletions'
                else:
                    _, deletes = mods
                    inserts = '0 insertions'

            yymm = YEAR_MONTH.format(y=dt.year, m=dt.month)
            res[yymm] += _get_int(inserts) + _get_int(deletes)

        most_common = res.most_common()
        return most_common[-1][0], most_common[0][0]