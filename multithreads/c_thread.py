# We may use any class as a thread, even if it does not inherit from Thread
from threading import Thread
import random
import time
import timeit

class SimpleClass():
    '''This is an ordinary class, but we may still make it threadable'''
    def __init__(self):
        pass # we could do the usual stuff here...
    # we write a __call__ medhod to be called by Thread
    def __call__(self, n, x):
        for _ in range(0,4):
            time.sleep(random.random()*(0.5*x))
        print(f'{n} is done')

if __name__ == '__main__':
    sc = SimpleClass()
    # we may need several threads
    thread_list = []
    for _ in range(0,1024):
        thread_list.append( Thread(target=sc, args=(_,0.3)) ) # this targets the __call__ of our class
    start = timeit.default_timer()
    # we need to start all our threads
    for _ in thread_list:
        _.start()
    for _ in thread_list:
        _.join()

    end = timeit.default_timer()
    print(f'Total execution time:{end-start} seconds')