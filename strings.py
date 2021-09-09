from typing import List


def common_words(sentence1: List[str], sentence2: List[str]) -> List[str]:
    """
    Input:  Two sentences - each is a  list of words in case insensitive ways.
    Output: those common words appearing in both sentences. Capital and lowercase 
            words are treated as the same word. 

            If there are duplicate words in the results, just choose one word. 
            Returned words should be sorted by word's length.
    """
    sentence1 = [word.lower() for word in sentence1] 
    sentence2 = [word.lower() for word in sentence2] 
    common_word = sorted(list(set(sentence1).intersection(set(sentence2))),key = len)
    return common_word


#pybites

def common_words(sentence1, sentence2) -> List[str]:
    sentence1_set = set(map(str.lower, sentence1))
    sentence2_set = set(map(str.lower, sentence2))
    commons = sentence1_set & sentence2_set
    return sorted(commons, key=len)

    