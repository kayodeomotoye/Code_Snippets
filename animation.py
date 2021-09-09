from itertools import cycle
import sys
from time import time, sleep

SPINNER_STATES = ['-', '\\', '|', '/']  # had to escape \
STATE_TRANSITION_TIME = 0.1


def spinner(seconds):
    """Make a terminal loader/spinner animation using the imports above.
       Takes seconds argument = time for the spinner to run.
       Does not return anything, only prints to stdout."""
    timeout = time()
    for state in cycle(SPINNER_STATES):
        if time() - timeout > seconds: break
        else:
            print(state, end= '\r', flush= True)
            sleep(STATE_TRANSITION_TIME)
           

#pybites
def spinner(seconds):
    symbols = cycle(SPINNER_STATES)
    end_time = time() + seconds
    while time() < end_time:
        # '\r' is needed to return cursor to start of the line
        sys.stdout.write('\r' + next(symbols))  # no newline
        sys.stdout.flush()
        sleep(STATE_TRANSITION_TIME)
    print()  # newline here            
           
             
        

if __name__ == '__main__':
    spinner(2)

