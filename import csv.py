import csv
from io import StringIO 

def split_words_and_quoted_text(text):
    """Split string text by space unless it is
       wrapped inside double quotes, returning a list
       of the elements.

       For example
       if text =
       'Should give "3 elements only"'

       the resulting list would be:
       ['Should', 'give', '3 elements only']
    """
    

data = StringIO(text) 
reader = csv.reader(data, delimiter=' ') 
for row in reader: 
    return row 


from shlex import split


def split_words_and_quoted_text(text):
    """Split string text by space unless it is
       wrapped inside double quotes, returning a list
       of the elements.

       For example
       if text =
       'Should give "3 words only"'

       the resulting list would be:
       ['Should', 'give', '3 words only']
    """
    return split(text)