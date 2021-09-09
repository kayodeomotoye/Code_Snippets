from dataclasses import dataclass


import dateutil
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta


@dataclass
class Actor:
    name: str
    born: str


@dataclass
class Movie:
    title: str
    release_date: str


def get_age(actor: Actor, movie: Movie) -> str:
    """Calculates age of actor / actress when movie was released,
       return a string like this:

       {name} was {age} years old when {movie} came out.
       e.g.
       Wesley Snipes was 28 years old when New Jack City came out.
    """
    actor_dob = parse(actor.born)
    movie_rel = parse(movie.release_date)
    age_at_rel = relativedelta(movie_rel, actor_dob).years
    return f"{actor.name} was {age_at_rel} years old when {movie.title} came out"


#pybites

def get_age(actor: Actor, movie: Movie) -> str:
    """Calculates age of actor / actress when movie was released,
       return a string like this:

       {name} was {age} years old when {movie} came out.
       e.g.
       Wesley Snipes was 28 years old when New Jack City came out.
    """
    age = relativedelta(parse(movie.release_date), parse(actor.born))
    return f'{actor.name} was {age.years} years old when {movie.title} came out.'
