from collections import Counter, namedtuple
import os
import urllib.request

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, 'dirnames')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/dirnames.txt',
    tempfile
)

IGNORE = 'static templates data pybites bbelderbos hobojoe1848'.split()
Stats = namedtuple('Stats', 'user challenge')


# Kayode's code
def gen_files(tempfile=tempfile):
    """
    Parse the tempfile passed in, filtering out directory names
    (first column) using the last "is_dir" column.

    Lowercase these directory names and return them as a generator.

    "tempfile" has the following format:
    challenge<int>/file_or_dir<str>,is_dir<bool>

    For example:
    03/rss.xml,False
    03/tags.html,False
    03/Mridubhatnagar,True
    03/aleksandarknezevic,True

    => Here you would return 03/mridubhatnagar (lowercased!)
       followed by 03/aleksandarknezevic
    """
    with open(tempfile) as f:
        content = f.readlines()
        for line in content:
            if 'true' in line.lower():
                result=line.split(',')[0].lower()
                yield result


def diehard_pybites(files=None):
    """
    Return a Stats namedtuple (defined above) that contains:
    1. the user that made the most pull requests (ignoring the users in IGNORE), and
    2. a tuple of:
        ("most popular challenge id", "amount of pull requests for that challenge")

    Calling this function on the default dirnames.txt should return:

    Stats(user='clamytoe', challenge=('01', 7))
    """
    if files is None:
        files = list(gen_files())
    user_pull = [line.split('/')[1] for line in files if line.split('/')[1] not in IGNORE]
    chall_pull = [line.split('/')[0] for line in files if line.split('/')[1] not in IGNORE]       
    user_pull_high = Counter(user_pull).most_common(1)[0][0]
    popular_challenges = Counter(chall_pull).most_common(1)[0]

    return Stats(user_pull_high, popular_challenges)



#pybites's code
def gen_files(tempfile=tempfile):
    with open(tempfile) as f:
        return (line.split(',')[0].lower()
                for line in f.readlines()
                if line.strip().endswith('True'))


def diehard_pybites(files=None):
    if files is None:
        files = gen_files()

    users = Counter()
    popular_challenges = Counter()

    for dir_ in files:
        ch, user = dir_.split('/')

        if user in IGNORE:
            continue

        users[user] += 1
        popular_challenges[ch] += 1

    user = users.most_common(1)[0][0]
    challenge = popular_challenges.most_common(1)[0]
    return Stats(user=user, challenge=challenge)