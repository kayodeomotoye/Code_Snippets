from collections import namedtuple
from itertools import cycle, islice
from time import sleep

State = namedtuple('State', 'color command timeout')

#kayode's
def traffic_light():
    """Returns an itertools.cycle iterator that
       when iterated over returns State namedtuples
       as shown in the Bite's description"""
    return cycle([State('red', 'Stop', 2), State('green', 'Go', 2),
                 State('amber', 'Caution', 0.5)])


#pybites'
def traffic_light():
    """Returns an itertools.cycle iterator that
       when iterated over returns State namedtuples
       as shown in the Bite's description"""
    colors = 'red green amber'.split()
    command = 'Stop Go Caution'.split()
    timings = (2, 2, 0.5)
    return cycle([State(*s) for s in
                  zip(colors, command, timings)])



if __name__ == '__main__':
    # print a sample of 10 states if run as standalone program
    for state in islice(traffic_light(), 10):
        print(f'{state.command}! The light is {state.color}')
        sleep(state.timeout)


