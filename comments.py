import re
def strip_comments(code):
    replaced = re.sub(r'(""")(?s).*?(""")' , '', class_three_indents)
    rmv_comment = re.sub(r'\s*\#\s+(.*)' , '', replaced)
    res1= re.sub(r'\s*\n','\n',rmv_comment, re.MULTILINE)
    res_string = '\ndef' 
    result= res1.replace('def', res_string)
    fin_result = re.sub(r'\n\s*\n','\n\n',result)
    return fin_result

strip_comments(class_three_indents)
#strip_comments(false_positive)
#strip_comments(class_with_method)

 rmv_comment = re.sub(r'\n\s*\#\s*(.*)' , '', replaced)
    print(re.sub(r'\n\s*\n','\n',rmv_comment,re.MULTILINE))
#s.replace('\n\n','\n')
#result= re.sub(r'\n\s*\n','\n',rmv_comment)


expected = "\nimport re\n\ndef hello(name):\n    return f'hello {name}'\n"
           "\nimport re\n\n    def hello(name):\n    return f'hello {name}'\n"
expected = "\nclass SimpleClass:\n\n    def say_hello(self, name: str):\n        print(f'Hello {name}')\n\n        def func_in_method(self):\n            pass\n"
           "\nclass SimpleClass:\n\ndef say_hello(self, name: str):\n        print(f'Hello {name}')\n\ndef func_in_method(self):\n            pass\n"


res_string = '\n' + 'def' 
res3= result.replace('def', res_string) 

single_comment = '''
def hello_world():
    # A simple comment preceding a simple print statement
    print("Hello World")
'''


single_docstring = '''
def say_hello(name):
    """A simple function that says hello... Richie style"""
    print(f"Hello {name}, is it me you're looking for?")
'''


class_with_method = '''
class SimpleClass:
    """Class docstrings go here."""

    def say_hello(self, name: str):
        """Class method docstrings go here."""
        print(f'Hello {name}')
'''

multiline_docstring = '''
def __init__(self, name, sound, num_legs):
    """
    Parameters
    ----------
    name : str
        The name of the animal
    sound : str
        The sound the animal makes
    num_legs : int, optional
        The number of legs the animal (default is 4)
    """
    self.name = name
    self.sound = sound
    self.num_legs = num_legs
'''


class_three_indents = '''
class SimpleClass:
    """Class docstrings go here."""

    def say_hello(self, name: str):
        """Class method docstrings go here."""
        print(f'Hello {name}')

        def func_in_method(self):
            """Docstring with 3 indents and multiline
               should also be stripped
            """
            pass
'''

false_positive = '''
def foo():
    # this is a comment
    print('this is not a #comment')
'''

code_bite_description = '''
"""this is
my awesome script
"""
# importing modules
import re

def hello(name):
    """my function docstring"""
    return f'hello {name}'  # my inline comment
'''
strip_comments(single_comment)




#pybites
import re


def strip_comments(code):
    # [\s\S]*? to rm docstring -> https://stackoverflow.com/a/44532145
    # \s* = 0 or more spaces
    # ?: is non-capturing (not needed but best practice)
    # *? is not being 'greedy' (match shortest possible pattern)
    # carrying over the newline to fix indenting issue
    return re.sub(r'(?:\s*#\s.*|\s{2}#\s.*|\s*"""[\s\S]*?""")(\n)',
                  r'\1', code, re.MULTILINE)