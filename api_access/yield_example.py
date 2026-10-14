# there is a keyword 'yield'
# It is primarily used to write custom generators
# but can be used more widely
import datetime

# range
r = range(-10**3,10**3,5) # start, stop-before, step=1

# generator
g = (i*i for i in r ) # yield every square of the numbers in the range 'r'

# comprehension
l = [i*i for i in r] # this creartes a list containnig all the values fro mthe generator

# custom generator
def makeDateTimeStamp():
    '''Generate a date-time stamp representing the moment this generator is invoked'''
    while True: # an endless loop
        t = datetime.datetime.now().strftime('%H:%M:%S:%f') # a date-time picture
        yield t # yield makes an ordinary function behave as a generator

if __name__ == '__main__':
    '''make use of the custom generator'''
    ts_gen = makeDateTimeStamp() # we now have an instance
    print( type(ts_gen) ) # we have a generator object
    print( type(g) ) # we have a generator object
    # we may access the next available member from a generator like this
    t = ts_gen.__next__()
    print(t)
    print( g.__next__() ) # 100000
    print( g.__next__() )
    print( g.__next__() )
    print( g.__next__() )
    print( g.__next__() )


