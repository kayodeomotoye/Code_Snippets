import pandas as pd
from datetime import date

def get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
  
    dates = sorted(dates)
    full_date_range=pd.date_range(start=dates[0], end=dates[-1])
    date_range =[pd.Timestamp(date) for date in dates]
    return [date.date() for date in full_date_range if pd.Timestamp(date) not in date_range] 



#pybites
from dateutil import rrule


def get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    start = min(dates)
    count = max(dates).day - start.day
    date_range = [d.date() for d in
                  rrule.rrule(rrule.DAILY, count=count,
                              dtstart=start)]
    return set(date_range) - set(dates)