import re
import string


def has_timestamp(text):
    """Return True if text has a timestamp of this format:
       2014-07-03T23:30:37"""
    if re.search(r'(\d+-\d\d-\d+T\d+:\d+:\d+)', text): return True
    else: return False


   
def is_integer(number):
    """Return True if number is an integer"""
    #if len[re.findall(r"\d+", number)] == 1: return True
    #else: return False
    number = str(number)
    if not re.match("^[0-9 -]+$", number): return   False
    else: return True


def has_word_with_dashes(text):
    """Returns True if text has one or more words with dashes"""
    if re.search(r'(\b-\b)', text): return True 
    else: return False


def remove_all_parenthesis_words(text):
    """Return text but without any words or phrases in parenthesis:
       'Good morning (afternoon)' -> 'Good morning' (so don't forget
       leading spaces)"""
    return re.sub(r"\s\((.*?)\)", '', text)


def split_string_on_punctuation(text):
    """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
       ['hi', 'how are you doing', 'blabla']
       (make sure you strip trailing spaces)"""
    puntuation_marks = string.punctuation
    return [line.strip(puntuation_marks).strip() for line in re.split(r"[.,?]",text, 2)] 

def remove_duplicate_spacing(text):
    """Replace multiple spaces by one space"""
    return re.sub(' +', ' ', text) 


def has_three_consecutive_vowels(word):
    """Returns True if word has at least 3 consecutive vowels"""
    pattern = r"[aeiou]{3}"
    result = re.findall(pattern, word)
    return result


def convert_emea_date_to_amer_date(date):
    """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
       (AMER date format)"""
    return re.sub(r'(\d{1,2})/(\d{1,2})/(\d{4})', '\\2/\\1/\\3', date)




#pybites

import re


def has_timestamp(text):
    """Return True if text has a timestamp of this format:
       2014-07-03T23:30:37"""
    return re.search(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}', text)


def is_integer(number):
    """Return True if number is an integer"""
    return re.match(r'-?\d+$', str(number))


def has_word_with_dashes(text):
    """Returns True if text has one or more words with dashes"""
    return re.search(r'\w+-\w+', text)


def remove_all_parenthesis_words(text):
    """Return text but without any words or phrases in parenthesis:
       'Good morning (afternoon)' -> 'Good morning' (so don't forget
       leading spaces)"""
    return re.sub(r' +\(.*?\)', r'', text)


def split_string_on_punctuation(text):
    """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
       ['hi', 'how are you doing', 'blabla']
       (make sure you strip trailing spaces)"""
    bits = re.split(r'[?!.,;]', text)
    return [bit.strip() for bit in bits if bit.strip()]


def remove_duplicate_spacing(text):
    """Replace multiple spaces by one space"""
    return re.sub(r' +', r' ', text)


def has_three_consecutive_vowels(word):
    """Returns True if word has at least 3 consecutive vowels"""
    return re.search(r'[aeiou]{3,}', word, re.IGNORECASE)


def convert_emea_date_to_amer_date(date):
    """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
       (AMER date format)"""
    return re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\2/\1/\3', date)