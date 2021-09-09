from collections import Counter
from operator import itemgetter
import requests

STOCK_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/stocks.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off, multiply by 1,000 and return
         value as float"""
    if cap == 'n/a': return 0 
    elif 'M' in cap: return float((cap.strip('$''M')))
    elif 'B' in cap: return float((cap.strip('$''B'))) * 1000
       
_cap_str_to_mln_float('n/a') 
_cap_str_to_mln_float('$100.45M') 
_cap_str_to_mln_float('$20.9B')

def get_industry_cap(industry):

    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
       
    for line in data:
        list1 = [round(_cap_str_to_mln_float(line['cap']), 2) for line in data if 
        line['industry'] == industry ]  
    return round(sum(list1), 2)

get_industry_cap('Business Services')
get_industry_cap("Real Estate Investment Trusts") 

def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    test_res= {line.get('symbol'): line.get('cap') for line in data if line['cap'] != 'n/a'}
    convt_dict = {k : _cap_str_to_mln_float(v) for k, v in test_res.items()}
    for k, v in convt_dict.items():
        if v == max(convt_dict.values()):
            return k
    
def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    sectors = Counter(map(itemgetter('sector'), data))
    ang = dict(sectors.most_common())
    new_min = min(list(ang.values())) 
    new_max= max(list(ang.values())[1:]) 
    for k, v in ang.items():
        if v == new_max:
            n_name = k
        
        elif v == new_min:
            l_name = k

    return n_name, l_name



    


#pybites

'''from collections import Counter

import requests

STOCK_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/stocks.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    stocks = s.get(STOCK_DATA).json()


# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    cap = cap.lstrip('$')
    if cap == 'n/a':
        return 0
    if 'M' in cap:
        return float(cap.replace('M', ''))
    if 'B' in cap:
        return float(cap.replace('B', '')) * 1000


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    ret = sum(_cap_str_to_mln_float(x["cap"])
              for x in stocks if x["industry"] == industry)
    return round(ret, 2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    stocks_sorted = sorted(stocks,
                           key=lambda x: _cap_str_to_mln_float(x["cap"]))
    return stocks_sorted[-1]['symbol']


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    cnt = Counter([x["sector"] for x in stocks
                   if x["sector"] != 'n/a']).most_common()
    return cnt[0][0], cnt[-1][0]'''