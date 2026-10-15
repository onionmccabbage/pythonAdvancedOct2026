# All threads share the same access to common resources
# This can be a problem when more than one thread tries to access a resource at the same moment
from threading import Thread
import random
import time
import timeit

class CodeRunnerDummy(Thread):
    '''This class illustrates the problem with resource access
    Here we pretend to execute code (e.g. tests, automation etc.)'''
    def __init__(self, n):
        Thread().__init__()
        self.n = n
        self.test_count = 0
    def run(self):
        while True: # a run loop - our Thread will run endlessly .... until we break
            '''if there are any scripts in the pool, take one and deal with it'''
            if len(scripts)>0:
                nextScript = scripts.pop() # grab the next available resource
                # here we could carry out the script
                self.randomDelay() # emulate a long runnig operation
                self.test_count +=1
            else:
                '''if there are no more resources, then this thread can end'''
                print(f'Script runner {self.n} completed {self.test_count} operations')
                break
    def randomDelay(self):
        '''sleep for a random short period (emulate a long running thing)'''
        time.sleep(random.randint(1,5)/4) # 0.25, 0.5, 0.75, 1


    
if __name__ == '__main__':
    '''exercise this module'''
    scripts = []
    # here is a bunch of 'scripts' - a resource for our thread class
    for _ in range(0,1024):
        s = {'id':_, 'kind':'Python'} # this stands in for our external scripts to be run
        scripts.append(s)
    # a bunch of threads to work on our scripts
    num_threads = 8
    runners_list = []
    for _ in range(0, num_threads):
        runner = CodeRunnerDummy(_)
        runners_list.append(runner)
    start = timeit.default_timer()
    for _ in runners_list:
        _.start()
    for _ in runners_list:
        _.join()
    end = timeit.default_timer()
    print(f'Total time: {end-start} seconds')
    
    

    