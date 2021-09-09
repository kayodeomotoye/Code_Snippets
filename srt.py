from datetime import time, timedelta
from typing import List
from dateutil.parser import parse


def get_srt_section_ids(text: str) -> List[int]:
    """Parse a caption (srt) text passed in and return a
       list of section numbers ordered descending by
       highest speech speed
       (= ratio of "time past:characters spoken")

       e.g. this section:

       1
       00:00:00,000 --> 00:00:01,000
       let's code

       (10 chars in 1 second)

       has a higher ratio then:

       2
       00:00:00,000 --> 00:00:03,000
       code

       (4 chars in 3 seconds)

       You can ignore milliseconds for this exercise.
    """
    split_text = [line.strip("\n").splitlines() for line in text.split("\n\n")]
    ret_dict = {
        line[0]: (
            (
                parse(line[1].split("-->")[1]) - parse(line[1].split("-->")[0])
            ).total_seconds()
        )
        / len(line[-1])
        for line in split_text
    }
    result = sorted(ret_dict, key = ret_dict.get) 
    return [int(line) for line in result] 



#pybites

from datetime import timedelta
from operator import itemgetter
from typing import List


def _create_timedelta(timestamp):
    """Convert timestamp to timedelta object"""
    ts = timestamp.split(',')[0]
    hh, mm, ss = ts.split(':')
    return timedelta(
        hours=int(hh),
        minutes=int(mm),
        seconds=int(ss))


def get_srt_section_ids(text: str) -> List[int]:
    ret = {}
    blocks = text.strip().split('\n\n')
    for block in blocks:
        section, timestamps, subtitle = block.splitlines()

        start, end = timestamps.split(' --> ')
        start_td = _create_timedelta(start)
        end_td = _create_timedelta(end)

        ratio = len(subtitle) / (end_td - start_td).seconds
        ret[int(section)] = ratio
    print(ret)
    return [k for k, _ in
            sorted(ret.items(), key=itemgetter(1),
                   reverse=True)]