from collections import namedtuple
from datetime import date, datetime, timedelta

TimeOffset = namedtuple('TimeOffset', 'offset date_str divider')

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60*60, 24*60*60
TIME_OFFSETS = (
    TimeOffset(10, 'just now', None),
    TimeOffset(MINUTE, '{} seconds ago', None),
    TimeOffset(2*MINUTE, 'a minute ago', None),
    TimeOffset(HOUR, '{} minutes ago', MINUTE),
    TimeOffset(2*HOUR, 'an hour ago', None),
    TimeOffset(DAY, '{} hours ago', HOUR),
    TimeOffset(2*DAY, 'yesterday', None),
)


def pretty_date(date):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    
    if type(date) != datetime or date > NOW:
        raise ValueError
    date_delta = (NOW - date)

    for line in TIME_OFFSETS:
        if line.divider != None:
            off_set = int(line.offset / line.divider)
            ref_date_delta = int((date_delta.days * DAY + date_delta.seconds)/line.divider)
        else: 
            off_set = line.offset
            ref_date_delta = date_delta.days * DAY + date_delta.seconds
            
        if ref_date_delta >=  2 * DAY:
            return date.strftime('%m/%d/%y')

        if ref_date_delta <  off_set:
           return line.date_str.format(ref_date_delta) 

       
#pybites
def pretty_date(date):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    if not isinstance(date, datetime) or date > NOW:
        raise ValueError('expecting past datetime')

    # using total_seconds because seconds only goes till max 1 day
    seconds = int((NOW - date).total_seconds())

    for time in TIME_OFFSETS:
        if seconds < time.offset:
            amount = time.divider and int(seconds/time.divider) or seconds
            return time.date_str.format(amount)
    else:
        # beyond yesterday just print date string
        return date.strftime('%m/%d/%y')