from datetime import date, datetime
from dateutil.rrule import rrule, YEARLY, SU
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta, SU

def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    start_date = datetime(year= year, month=1, day=1)
    return list(rrule(YEARLY, count=1, bymonth=5, byweekday=SU(2), dtstart=start_date))[0].date()



#Pybites
MAY = 5


def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    first_of_may = date(year=year, month=MAY, day=1)
    return first_of_may + relativedelta(weeks=1, weekday=SU)