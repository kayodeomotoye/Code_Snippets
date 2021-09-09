import json
from pathlib import Path
from urllib.request import urlretrieve


TMP = Path('')
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DATA = 'omdb_data'

DATA_LOCAL = TMP / DATA
if not Path(DATA_LOCAL).exists():
    urlretrieve(S3 + DATA, DATA_LOCAL)


def get_movie_data(files: list = None) -> list:
    """Parse movie json files into a list of dicts"""
    files = []
    with open(DATA_LOCAL) as f:
        for line in f.readlines():
            files.append(json.loads(line))
    return files


def get_single_comedy(movies: list = None) -> str:
    """return the movie with Comedy in Genres"""
    return [line['Title'] for line in get_movie_data() if 'Comedy' in line['Genre'].split(',')][0] 


def get_movie_most_nominations(movies: list = None) -> str:
    """Return the movie that had the most nominations"""
    
    ret_movies = [line['Awards'].split('&') for line in get_movie_data()]
    nom_order = sorted([line[1] for line in ret_movies], key = lambda x : int(x.split()[0]), reverse = True)
    return [line['Title'] for line in get_movie_data() if nom_order[0] in line['Awards']][0]


def get_movie_longest_runtime(movies: list = None) -> str:
    """Return the movie that has the longest runtime"""
    max_runtime = max([int(line['Runtime'].strip('min')) for line in get_movie_data()])
    return [line['Title'] for line in get_movie_data() if int(line['Runtime'].strip('min')) == max_runtime][0]


#pybites

import json
import re


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movies = []
    for fi in files:
        with open(fi) as f:
            json_ = json.loads(f.read())
        movies.append(json_)
    return movies


def _grep_movies(movies, key):
    for movie in movies:
        yield movie.get('Title'), movie.get(key)


def get_single_comedy(movies: list) -> str:
    """Return the movie with Comedy in Genres"""
    movies = dict(_grep_movies(movies, 'Genre'))
    comedies = {k: v for k, v in movies.items() if 'Comedy' in v}
    return list(comedies.keys())[0]


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    movies = dict(_grep_movies(movies, 'Awards'))
    extract_nominations = lambda m: int(re.sub(r'.*\s(\d+)\snomin.*', r'\1', m[1]))  # noqa E731 E501
    return max(movies.items(), key=extract_nominations)[0]


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    movies = dict(_grep_movies(movies, 'Runtime'))
    extract_runtime = lambda m: int(m[1].split()[0])  # noqa E731
    return max(movies.items(), key=extract_runtime)[0]

