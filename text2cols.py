# importing pandas module  
import textwrap
from tabulate import tabulate

#text = """My house is small but cosy."""
'''text = """My house is small but cosy.

    It has a white kitchen and an empty fridge.

    I have a very comfortable couch, people love to sit on it.

    My mornings are filled with coffee and reading, if only I had a garden""" '''

text = """My house is small but cosy.

        It has a white kitchen and an empty fridge."""

def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""
    
    dedented_txt = textwrap.dedent(text).strip()
    dedented_text = dedented_txt.splitlines()
    for line in dedented_text:
        ded_list = [textwrap.fill(line.strip(), initial_indent='', subsequent_indent='', width=20) for line in dedented_text]    
    ded_list2=[]
    ded_list2.append(ded_list)
    return print(tabulate(ded_list2, tablefmt ='plain'))
            


#pybites
from itertools import zip_longest
import textwrap

COL_WIDTH = 20
PADDING = 5


def _format(row):
    return " ".join(['{c:{w}}'.format(c=col, w=COL_WIDTH+PADDING)
                     for col in row])


def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""
    cols = []
    for paragraph in text.split("\n\n"):
        col_lines = textwrap.fill(paragraph, width=COL_WIDTH).split("\n")
        cols.append(col_lines)

    output = []
    # need zip_longest otherwise text will get lost
    for row in zip_longest(*cols, fillvalue=''):
        output.append(_format(row))
    
    return "\n".join(output)



    >>> text_to_columns(text)
'My house is small        \nbut cosy.     It has     \na white kitchen and      \nan empty fridge.         \nI have a very            \ncomfortable couch,       \npeople love to sit  
     \non it.     My            \nmornings are filled      \nwith coffee and          \nreading, if only I       \nhad a garden             '