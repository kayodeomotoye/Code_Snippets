from datetime import date
from operator import attrgetter
from typing import Dict, Sequence, NamedTuple, Counter


class MovieRented(NamedTuple):
    title: str
    price: int
    date: date


RentingHistory = Sequence[MovieRented]
STREAMING_COST_PER_MONTH = 12
STREAM, RENT = 'stream', 'rent'


def rent_or_stream(
    renting_history: RentingHistory,
    streaming_cost_per_month: int = STREAMING_COST_PER_MONTH
) -> Dict[str, str]:
    """Function that calculates if renting movies one by one is
       cheaper than streaming movies by months.

       Determine this PER MONTH for the movies in renting_history.

       Return a dict of:
       keys = months (YYYY-MM)
       values = 'rent' or 'stream' based on what is cheaper

       Check out the tests for examples.
    """
    
    ret_dict = {}
    price_dict ={}
    ret_value = 0
    for line in renting_history:
        ret_key = date.strftime(line.date, "%Y-%m")
        ret_value += line.price
        price_dict[ret_key] = ret_value
        if price_dict[ret_key] > streaming_cost_per_month:ret_dict[ret_key] = STREAM 
        else: ret_dict[ret_key] = RENT

    return ret_dict

 


#pybites

def rent_or_stream(
    renting_history: RentingHistory,
    streaming_cost_per_month: int = STREAMING_COST_PER_MONTH
) -> Dict[str, str]:
    month_costs: Counter[str] = Counter()
    for movie in renting_history:
        date = movie.date
        key = f"{date.year}-{date.month}"
        month_costs[key] += movie.price

    return {
        ym: STREAM if cost > streaming_cost_per_month else RENT
        for ym, cost in month_costs.items()