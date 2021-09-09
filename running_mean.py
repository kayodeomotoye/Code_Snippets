from itertools import islice
import statistics

def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    avg_list=[]
    new_list = []
    for num in sequence:
        new_list.append(num)
        avg = round(statistics.mean(new_list), 2)
        avg_list.append(avg)
    
    return avg_list
        
               
        
#pybites

from itertools import accumulate


def running_mean_old(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    if not sequence:
        return []

    total = 0
    running_mean = []

    for i, num in enumerate(sequence, 1):
        total += num
        mean = round(total/i, 2)
        running_mean.append(mean)

    return running_mean


def running_mean(sequence):
    """Same functionality as above but using itertools.accumulate
       and turning it into a generator"""
    for i, num in enumerate(accumulate(sequence), 1):
        yield round(num/i, 2)


[3, 4, 6, 2, 1, 9, 0, 7, 5, 8]