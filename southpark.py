from collections import Counter, defaultdict
import csv
import requests

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv' # noqa E501


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode('utf-8')


def get_num_words_spoken_by_character_per_episode(content):
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""
    ret_dict = defaultdict(Counter)
    res_split_dict = csv.DictReader(content.splitlines())
    for line in res_split_dict:
        character = line['Character']
        episode = line['Episode']
        words = line['Line'].split()
        res_dict = {}
        res_dict[episode] = len(words)
        ret_dict[character].update(Counter(res_dict))
        
    return ret_dict

#pybites
def get_num_words_spoken_by_character_per_episode(content):
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""
    reader = csv.DictReader(content.splitlines(), delimiter=',')

    # nested collections: https://stackoverflow.com/a/5029958
    words_spoken = defaultdict(lambda: Counter())

    for row in reader:
        episode = row['Episode']
        character = row['Character']
        words = row['Line'].rstrip().split()
        words_spoken[character][episode] += len(words)

    return words_spoken