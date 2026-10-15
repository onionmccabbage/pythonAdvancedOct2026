# All threads share the same access to common resources
# This can be a problem when more than one thread tries to access a resource at the same moment
from threading import Thread
from threading import Lock
import random
import time
import timeit

# a common problem with threading: a single resource with multiple thread access
# There is a non-zero chance that more than one thread 
# may try to access the resource at the same time
# Since Python 3.13 this is less of an issue, but...
# It is still best to implement Thread Locks


class CodeRunnerDummy(Thread):
    '''This class illustrates the problem with resource access
    Here we pretend to execute code (e.g. tests, automation etc.)'''
    def __init__(self, n, l):
        Thread.__init__(self)
        self.n = n
        self.lock = l # grab the lock instance (same lock will be shared by all threads)
        self.test_count = 0
    def run(self):
        while True: # a run loop - our Thread will run endlessly .... until we break
            '''if there are any scripts in the pool, take one and deal with it'''
            if len(scripts)>0:
                nextScript = scripts.pop() # grab the next available resource
                # here we could carry out the script
                self.randomDelay() # emulate a long runnig operation
                self.lock.acquire() # this gives unique access to the locked resource
                self.test_count +=1
            else:
                '''if there are no more resources, then this thread can end'''
                print(f'Script runner {self.n} completed {self.test_count} operations')
                break
            self.lock.release() # at the earliest opportunity we release the shared lock
    def randomDelay(self):
        '''sleep for a random short period (emulate a long running thing)'''
        time.sleep(random.randint(1,5)/400) # 0.0025, 0.005, 0.0075, 0.01
    
if __name__ == '__main__':
    '''exercise this module'''
    lock = Lock() # here is an instance of the Lock used for unique thread resource access

    scripts = []
    # here is a bunch of 'scripts' - a resource for our thread class
    for _ in range(0,2056):
        s = {'id':_, 'kind':'Python'} # this stands in for our external scripts to be run
        scripts.append(s)
    # a bunch of threads to work on our scripts
    num_threads = 512
    runners_list = []
    for _ in range(0, num_threads):
        runner = CodeRunnerDummy(_, lock) # pass the same lock instance to all threads
        runners_list.append(runner)
    start = timeit.default_timer()
    for _ in runners_list:
        _.start()
    for _ in runners_list:
        _.join()
    end = timeit.default_timer()
    print(f'Total time: {end-start} seconds')
    
    

    