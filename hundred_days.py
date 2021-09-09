from datetime import date, datetime
from months import START_DATE
from dateutil.rrule import *

TODAY = date(year=2018, month=11, day=29)


def get_hundred_weekdays(start_date=TODAY):
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    
    set = rruleset()
    set.rrule(rrule(DAILY, count=140, dtstart=start_date))
    set.exrule(rrule(YEARLY, byweekday=(SA,SU), dtstart=start_date))
    return [datetime.date(line) for line in list(set)]


#pybites

def get_hundred_weekdays(start_date=TODAY):
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    date_range = rrule(DAILY, count=100,
                       byweekday=(MO, TU, WE, TH, FR),
                       dtstart=start_date)
    return [dt.date() for dt in date_range]


