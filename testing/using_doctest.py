# doctest is a simple testing shcema 
import doctest

def square(n=3):
    '''return the square of n (a number)
    >>> square(2)
    4
    >>> square(-3)
    9
    '''
    return n**2

if __name__ == '__main__':
    c = square(8) # 64
    print(c)
    # invoke doctest like this
    doctest.testmod(verbose=True)