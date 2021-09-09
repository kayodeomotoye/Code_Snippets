from collections import Counter, namedtuple
import csv
import re
import requests

MARVEL_CSV = "https://raw.githubusercontent.com/pybites/marvel_challenge/master/marvel-wikia-data.csv"  # noqa E501

Character = namedtuple("Character", "pid name sid align sex appearances year")


# csv parsing code provided so this Bite can focus on the parsing


def _get_csv_data():
    """Download the marvel csv data and return its decoded content"""
    with requests.Session() as session:
        return session.get(MARVEL_CSV).content.decode("utf-8")


def load_data():
    """Converts marvel.csv into a sequence of Character namedtuples
    as defined above"""
    content = _get_csv_data()
    reader = csv.DictReader(content.splitlines(), delimiter=",")
    for row in reader:
        name = re.sub(r"(.*?)\(.*", r"\1", row["name"]).strip()
        yield Character(
            pid=row["page_id"],
            name=name,
            sid=row["ID"],
            align=row["ALIGN"],
            sex=row["SEX"],
            appearances=row["APPEARANCES"],
            year=row["Year"],
        )


characters = list(load_data())


# start coding


def most_popular_characters(characters=characters, top=5):
    """Get the most popular character by number of appearances,
    return top n characters (default 5)
    """
    return [character[0].name for character in Counter(characters).most_common(top)]


def max_and_min_years_new_characters(characters=characters):
    """Get the year with most and least new characters introduced respectively,
    use either the 'FIRST APPEARANCE' or 'Year' column in the csv
    characters, or the 'year' attribute of the namedtuple, return a tuple
    of (max_year, min_year)
    """
    ret_dict = dict(
        Counter([character.year for character in characters if len(character.year) > 0])
    )
    min_year = sorted([
        key for key, value in ret_dict.items() if value == min(ret_dict.values())
    ], reverse = True)[0]
    max_year = [
        key for key, value in ret_dict.items() if value == max(ret_dict.values())
    ][0]
    return max_year, min_year


def get_percentage_female_characters(characters=characters):
    """Get the percentage of female characters as percentage of all genders
    over all appearances.
    Ignore characters that don't have gender ('sex' attribue) set
    (in your characters data set you should only have Male, Female,
    Agender and Genderfluid Characters.
    Return the result rounded to 2 digits
    """

    new_character = [character for character in characters if character.sex != ""]
    total_characters = len(new_character)
    female_characters = len(
        [
            character
            for character in new_character
            if character.sex == "Female Characters"
        ]
    )
    return round((female_characters / total_characters) * 100, 2)





#pybites

def most_popular_characters(characters=characters, top=5):
    """Get the most popular character by number of appearances,
       return top n characters (default 5)
    """
    # pre-filter characters, generator expressions reduce memory footprint
    appearances = (character for character in characters
                   if character.appearances.isdigit())
    top_characters = sorted(appearances, key=lambda x: int(x.appearances),
                            reverse=True)[:top]
    return [character.name for character in top_characters]


def max_and_min_years_new_characters(characters=characters):
    """Get the year with most and least new characters introduced respectively,
       use either the 'FIRST APPEARANCE' or 'Year' column in the csv
       characters, or the 'year' attribute of the namedtuple, return a tuple
       of (max_year, min_year)
    """
    most_common = Counter(character.year for character in characters
                          if character.year).most_common
    return most_common(1)[0][0], most_common()[-1][0]


def get_percentage_female_characters(characters=characters):
    """Get the percentage of female characters as percentage of all genders
       over all appearances.
       Ignore characters that don't have gender ('sex' attribue) set
       (in your characters data set you should only have Male, Female,
       Agender and Genderfluid Characters.
       Return the result rounded to 2 digits
    """
    sexes = Counter(character.sex for character in characters if character.sex)
    return round(
        sexes['Female Characters'] / sum(sexes.values()) * 100, 2
    )