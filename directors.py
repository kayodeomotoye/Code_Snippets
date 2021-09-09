import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve
import statistics   

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = ''

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    with open('movie_metadata.csv', encoding='utf-8') as f:
        r = csv.DictReader(f)
        d = defaultdict(list)
        tup_list=[]
        for row in r:
            if  '' in (Movie(row['movie_title'], row['title_year'], row['imdb_score'])):
                continue
            elif int(row['title_year']) >= MIN_YEAR:
                Movie_tup = Movie(row['movie_title'], int(row['title_year']), float(row['imdb_score']))
                d[row['director_name']].append(Movie_tup)
                
        #print(d['Peter Jackson'])
        return d
                  
dir_mov = get_movies_by_director()
def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    avg = round(statistics.mean([float(value[2]) for value in movies]), 1)
    return avg


def get_average_scores(directors = dir_mov):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    res_list =[]
    for director in dir_mov.keys():
        if len(dir_mov[director]) >= MIN_MOVIES:
            avg = round(statistics.mean([float(value[2]) for value in dir_mov[director]]), 1)
            res_list.append((director, avg))

    return sorted(res_list, key = lambda x: x[1], reverse =True)
    
    
 #pybites

def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    directors = defaultdict(list)
    with open(MOVIE_DATA) as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue
            if year and year < MIN_YEAR:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    ratings = [m.score for m in movies]
    mean = sum(ratings) / max(1, len(ratings))
    return round(mean, 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    ret = {director: calc_mean_score(movies)
           for director, movies in directors.items()
           if len(movies) >= MIN_MOVIES}
    return sorted(ret.items(), key=lambda x: x[1], reverse=True)   
    
    
