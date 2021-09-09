IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    newlist = []
    for name in names:
        if not name.isalpha():
            continue

        elif name[0] == QUIT_CHAR:
            break     

        elif name[0] != IGNORE_CHAR:
            newlist.append(name)

    return newlist[:MAX_NAMES]


list1 = ['bob', 'berta']
list2= ['12', 'bas']
list3 = ['ana', 'bob', 'ti2m', 'ajhh', 'iyu', 'jhut', 'rt6u']
list4 = ['aja', 'quinton', 'jhg']

filter_names(list1)
filter_names(list2)
filter_names(list3)
filter_names(list4)
            
'''
#pybites
def _name_has_digit(name):
    return any(c.isdigit() for c in name)


def filter_names(names):
    count = 0
    for name in names:
        if name.startswith(IGNORE_CHAR) or _name_has_digit(name):
            continue
        elif name.startswith(QUIT_CHAR) or count >= MAX_NAMES:
            break
        count += 1
        yield name'''