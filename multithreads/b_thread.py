# we may also use Threads with classes
from threading import Thread
import time
import random
import timeit

class MyClass(Thread): # when we inherit from Thread we MUST override the 'run' method
    '''This class extends the basic Thread class'''
    def __init__(self, n ,x): # we may pass args, kwargs etc.
        # if we invoke super() we are obliged to pass all the parameters 
        # super().__init__(group, target, name, args, kwargs, daemon=daemon)
        # instead call the Thread class directly (avoids unneeded arguments)
        Thread.__init__(self)
        self.n = n # we could write get/set decorators for these properties
        self.x = x
    def run(self):
        '''When this class is invoked as a Thread, the run method will be called'''
        # emulate exeution of four long-running steps
        for _ in range(0,4):
            print(f'{self.n} is sleeping') # try to avoid I/O bound operations in threads!
            time.sleep(random.random()*self.x)

if __name__ == '__main__':
    tA = MyClass('A', 1)
    tB = MyClass('B', 2)
    tC = MyClass('C', 0.5)
    start = timeit.default_timer()
    tA.start() # this invokes our run method
    tB.start()
    tC.start()
    tA.join()
    tB.join()
    tC.join()
    end = timeit.default_timer()
    print(f'Total time: {end-start} seconds')