# threading is easy in Python
from threading import Thread
import time
import random


def fn(n):
    '''A typical function (any function may be run on a new thread)'''
    r = random.randint(0,5)/50
    time.sleep( r ) # this will pause for a short time
    print(f'{n} completed in {r}')

if __name__ == '__main__':
    '''we may execute any function as a threada of control'''
    tA = Thread(target=fn, args=(1,) )

    # we may start the thread at any moment
    tA.start() # this is where the new thread begins to run