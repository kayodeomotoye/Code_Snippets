import os
import urllib.request
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)


def get_harry_most_common_word():
    with open(harry_text, encoding = 'utf-8') as f:
        content = f.read().lower().rstrip("'s").split()

    with open(stopwords_file) as t:
        content2 = t.read().splitlines()

    res = [value.rstrip("s").rstrip("'") for value in content if value not in content2]
    return Counter(res).most_common(1)[0]



#pybites

def get_harry_most_common_word():
    with open(stopwords_file) as f:
        stopwords = set(f.read().strip().lower().split('\n'))

    with open(harry_text) as f:
        words = [re.sub(r'\W+', r'', word)  # [^a-zA-Z0-9_]
                 for word in f.read().lower().split()]

        words = [word for word in words if word.strip()
                 and word not in stopwords]

        cnt = Counter(words)
        return cnt.most_common(1)[0]


  


