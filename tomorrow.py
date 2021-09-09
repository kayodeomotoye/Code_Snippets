import datetime

def tomorrow(date_object = 0):
    if date_object:
        answer = date_object + datetime.timedelta(1)
    else:
        answer = datetime.datetime.now().date()+ datetime.timedelta(days=1)
    return answer
    


#pybites

    """
    Figures out what the day after today is.

    :param asof: date to use as today in calculations
    :keyword asof:
    :type asof: datetime.date
    :return: a date object representing tomorrows date
    :rtype: datetime.date
    """
    if asof is None:
        asof = datetime.date.today()
    return asof + datetime.timedelta(days=1)