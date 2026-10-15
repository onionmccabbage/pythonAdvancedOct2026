# the idea of a 'daemon' goes back to the early history of computing
# it is the notition of a program that runs endlessly
# by default all Python threads are not daemon threads

from threading import Thread 
import time # we will use this simply to sleep

def standardThreadFn():
    '''This is a normal function, we will invke it on a non-daemon thread (the default)'''
    print('starting normal function')
    time.sleep(4)
    print('ending normal function')

# use cases:
# - constantly monitoring a running python program
# - showing a keep-alive heartbeat
# - regularly tidying up of commiting data somewhere
def daemonThreadFn():
    '''This is also a normal function, we will invoke it as a daemon thread (run endlessly)'''
    print('starting a function as a daemon thread')
    while True:
        print('heartbeat...')
        time.sleep(0.5)

if __name__ == '__main__':
    '''exercise our module'''
    s = Thread(target=standardThreadFn) # a standard thread (daemon defaults to None)
    d = Thread(target=daemonThreadFn, daemon=True) # this will run endlessly
    s.start()
    d.start()
    s.join()
    # if we wait for a daemon thread to join the main htread, it will NEVER rejoin
    # d.join() # this is redundant! We usually do not join a daemon thread
    # We simply allow the main htread to end, which automatically ends all other threads