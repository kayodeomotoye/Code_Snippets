from datetime import timedelta, date, datetime
import pandas as pd
from io import StringIO
import re
from dateutil.parser import *


TODAY = date(2018, 11, 12)


def extract_dates(data):
    """Extract unique dates from DB table representation as shown in Bite"""
    #return [datetime.strptime(date, "%Y-%m-%d").date() for date in re.findall(r"\d+-\d+-\d+", data)]
    return [date.fromisoformat(date_) for date_ in re.findall(r"\d+-\d+-\d+", data)]
    
   


def calculate_streak(dates):
    """Receives sequence (set) of dates and returns number of days
       on coding streak.

       Note that a coding streak is defined as consecutive days coded
       since yesterday, because today is not over yet, however if today
       was coded, it counts too of course.

       So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
       the table makes for a 3 days coding streak.

       See the tests for more examples that will be used to pass your code.
    """
    result = extract_dates(data3)
    result.insert(0, TODAY)
    
    ret_list =[]
    for idx in range(0, len(result)):
        if result[idx] == result[-1]:
            continue
        

        elif (result[idx] - timedelta(days=1) != result[idx+1]):
            ret_list.append('break')
            
            
        else:
            ret_list.append(result[idx])
            
        
#pybites

def _parse_date(line):
    date_str = line.lstrip(' |').split('|')[0].strip()
    return datetime.strptime(date_str, '%Y-%m-%d').date()


def extract_dates(data):
    """Extract unique dates from DB table representation as shown in Bite"""
    return {_parse_date(line) for line in data.splitlines()
            if line.strip().startswith('| 20')}


def calculate_streak(dates):
    """Receives sequence (set) of dates and returns number of days
       on coding streak.

       Note that a coding streak is defined as consecutive days coded
       since yesterday, because today is not over yet, however if today
       was coded, it counts too of course.

       So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
       the table makes for a 3 days coding streak.

       See the tests for more examples that will be used to pass your code.
    """
    streak = 0

    for i in range(1, len(dates) + 1):
        if TODAY - timedelta(days=i) in dates:
            streak += 1
        else:
            break

    if TODAY in dates:
        streak += 1
