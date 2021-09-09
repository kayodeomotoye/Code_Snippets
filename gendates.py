from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    for index in range(100,10000, 100):
        delta = timedelta(days=index)
        yield PYBITES_BORN + delta
       
    


#pybites

def gen_special_pybites_dates():
    days = 0
    while True:
        days += 1
        if days % 100 == 0:
            yield PYBITES_BORN + timedelta(days=days)
