from datetime import datetime, timedelta, time
import os
import re
import urllib.request

# getting the data
COURSE_TIMES = os.path.join(
    os.getenv("TMP", "/tmp"),
    'course_timings'
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/course_timings',
    COURSE_TIMES
)


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    course_duration = re.compile(r'\((.*?)\)')
    with open(COURSE_TIMES) as f:
        return course_duration.findall(f.read())


def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    full_time = ["00:" + line.zfill(5) for line in timestamps] 
    formatted_times = [time.fromisoformat(duration) for duration in full_time]
    minutes = sum([t.minute for t in formatted_times])
    seconds = sum([t.second for t in formatted_times])
    hrs = minutes//60
    min = minutes%60 + seconds//60 
    secs = seconds%60
    result = time(hour=hrs, minute=min, second=secs)
    return result.strftime("%H:%M:%S")


#pybites

def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    with open(COURSE_TIMES) as f:
        content = f.read()
        return re.findall(r'\d+:\d+', content)


def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    result = timedelta(minutes=0, seconds=0)

    for mm_ss in timestamps:
        minutes, seconds = mm_ss.split(':')
        result += timedelta(minutes=int(minutes), seconds=int(seconds))

    return str(result)