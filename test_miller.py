def _py2_earth_seconds_left(start_date):
    """How many earth seconds has Python 2 left?"""
    return (PY2_DEATH_DT - start_date).total_seconds()


def _convert_to_miller_seconds(earth_seconds):
    """1 hour on planet Miller == 7 years on planet Earth"""
    return earth_seconds/EARTH_TO_MILLER_RATIO


def py2_earth_hours_left(start_date=BITE_CREATED_DT):
    """Return how many hours, rounded to 2 decimals, Python 2 has
       left on Planet Earth (calculated from start_date)"""
    earth_seconds = _py2_earth_seconds_left(start_date)
    return round(earth_seconds / 3600, 2)


def py2_miller_min_left(start_date=BITE_CREATED_DT):
    """Return how many minutes, rounded to 2 decimals, Python 2 has
       left on Planet Miller (calculated from start_date)"""
    earth_seconds = _py2_earth_seconds_left(start_date)
    miller_seconds = _convert_to_miller_seconds(earth_seconds)
    return round(miller_seconds / 60, 2)