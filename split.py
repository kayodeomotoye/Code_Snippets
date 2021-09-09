import re


def get_sentences(text):
    """Return a list of sentences as extracted from the text passed in.
       A sentence starts with [A-Z] and ends with [.?!]"""
    split_text = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', text) 
    return [(re.sub('\n', ' ', line)).strip() for line in split_text]

    

#pybites

def get_sentences(text):
    """Return a list of sentences as extracted from the text passed in.
       A sentence starts with [A-Z] and ends with [.?!]"""
    sentences = re.findall(r'[A-Z].*?[.?!](?= [A-Z]|$)',  # use look-ahead
                           text.strip().replace('\n', ' '),
                           flags=re.DOTALL)
    return [sentence.strip() for sentence in sentences]