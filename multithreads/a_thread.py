# threading is easy in Python
from threading import Thread
import time
import random


def fn(n):
    '''A typical function (any function may be run on a new thread)'''
    r = random.randint(0,5)/50+0.001
    time.sleep( r ) # this will pause for a short time
    # NB we try to avoid I/O bound operations on separate threads
    print(f'{n} completed in {r}') # NB print() must return to the main thread

if __name__ == '__main__':
    '''we may execute any function as a threada of control'''
    tA = Thread(target=fn, args=(1,) )
    tB = Thread(target=fn, args=(2,) )

    # we may start the thread at any moment
    tA.start() # this is where the new thread begins to run
    tB.start() 

    # when does this next line execute
    print('Main thread is still running')
    # optionally we may choose to pause the main thread until other threads rejoin it
    tA.join()
    tB.join()
    print('Main thread continues only after other threads have rejoined')