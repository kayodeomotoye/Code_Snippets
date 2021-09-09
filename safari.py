from collections import defaultdict
import os
import urllib.request

TMP = os.getenv("TMP", "/tmp")
DATA = "safari.logs"
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = "🐍", "."

urllib.request.urlretrieve(
    f"https://bites-data.s3.us-east-2.amazonaws.com/{DATA}", SAFARI_LOGS
)


def create_chart():
    with open(SAFARI_LOGS) as file:
        new_file = file.readlines()
        print_dict = defaultdict(list)
        for line in new_file:
            date = line.split()[0]
            next_line = new_file[new_file.index(line) + 1]
            if (
                date in line
                and "Python" in line
                and "sending to slack channel" in next_line
            ):
                print_dict[date].append(PY_BOOK)
            elif (
                date in line
                and "Python" not in line
                and "sending to slack channel" in next_line
            ):
                print_dict[date].append(OTHER_BOOK)

    for _date, symbols in print_dict.items():
        print(_date + " ", "".join(symbols), sep="")
        



#pybites

def _get_lines(log):
    with open(log) as f:
        return [line.strip() for line in f.readlines()]


def create_chart(log=None):
    log = log or SAFARI_LOGS
    lines = _get_lines(log)

    posts = defaultdict(list)

    for prev_line, line in zip(lines, lines[1:]):
        if 'sending to' in line:
            date = prev_line.split()[0]
            book_icon = 'python' in prev_line.lower() and PY_BOOK or OTHER_BOOK
            posts[date].append(book_icon)

    for date, books in posts.items():
        print(date, ''.join(books))

                
create_chart()


                
                


        
        