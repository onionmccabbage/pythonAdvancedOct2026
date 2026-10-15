# threading is easy in Python
from threading import Thread
import time # time will read the computer clock
import timeit # timeit is able to ignore those times when Python is interrupted
import random


def fn(n):
    '''A typical function (any function may be run on a new thread)'''
    r = 0.02 # random.randint(0,5)/50+0.001
    time.sleep( r ) # this will pause for a short time
    # NB we try to avoid I/O bound operations on separate threads
    print(f'{n} completed in {r}') # NB print() must return to the main thread

if __name__ == '__main__':
    '''we may execute any function as a threada of control'''
    tA = Thread(target=fn, args=(1,) ) # we may also pass kwargs
    tB = Thread(target=fn, kwargs={'n':2} ) # kwargs are always a dict
    tC = Thread(target=fn, args=(3,) )
    tD = Thread(target=fn, args=(4,) )

    start = timeit.default_timer() # grab a moment in time

    # we may start the thread at any moment
    tA.start() # this is where the new thread begins to run
    tB.start() 
    tC.start() 
    tD.start() 

    # when does this next line execute
    print('Main thread is still running')
    # optionally we may choose to pause the main thread until other threads rejoin it
    tA.join()
    tB.join()
    tC.join()
    tD.join()
    end = timeit.default_timer()
    print(f'All operations completed in {end-start} seconds')