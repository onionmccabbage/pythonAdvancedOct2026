# We may send event notifications to threads, which can respond to these events
# thread events may be originated on the main thread
# other threads can simply receive this event
# there is no mechanism for threads to communicate or pass data

from threading import Thread, Event
import time

class MyClass:
    def __call__(self, n):
        '''We need access to the one event instance'''
        global e # this is now a pointer to the 'e' declared elsehwere
        print(f'{n} is waiting for an event flag notification')
        e.wait() # this thread will not proceed until the event flag is True
        print(f'{n} received the flag event, thread continues')

if __name__ == '__main__':
    '''exercise this module'''
    e = Event() # we have an instance of a Thread Event
    # m1 = MyClass()
    # m2 = MyClass()
    # t1 = Thread(target=m1, args=('A',))
    # t2 = Thread(target=m2, args=('B'))
    # we may have many threads
    th = []
    for _ in range(0,1024):
        m = MyClass()
        th.append(Thread(target=m, args=(_, )))
    for _ in th:
        _.start()

    # t1.start()
    # t2.start()

    # wait on the main thread
    time.sleep(3)

    # Can we respond to the event on the main thread
    # e.wait() # NO!!!! the main thread would never get round to setting the event

    # we may choose to set the event flag to True
    e.set()

    for _ in th:
        _.join()

    # t1.join() # careful - do not try to join until after setting the flag event!!!
    # t2.join()