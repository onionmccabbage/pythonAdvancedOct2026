# there are higher-order functions built in to Python
# (functions which take functions as arguments)
# map and filter are higher-order funcions, taking other functions as arguments

def isEven(n):
    '''Return True for all odd values of n, and False in every other case'''
    if n/2 == n//2:
        return True # it is even
    else:
        return False # it is not even

# NB we would probably want to validate the values before operating on them!
def squareIt(m):
    '''return the square of m'''
    return m**2

if __name__ == '__main__':
    oe1 = isEven(3)
    oe2 = isEven(4)
    print(oe1, oe2)
    # we may use this function repeatedly across a collection of values, using 'filter'
    d = (4,99,-3,12,42,-8,0)
    evens = list( filter(isEven, d) ) # make a list from the filter object
    print(evens) 
    # next we use our squareIt function to map across a collection of values
    squares = tuple( map(squareIt, d) ) # make a tuple from the results of the map object
    print(squares)
    # we are not restricted by any quantity of data (other than the machine capabilites)
    biggy = range(-10**6, 10**6, 1000)
    lotsOResults = filter(isEven, map(squareIt, biggy))