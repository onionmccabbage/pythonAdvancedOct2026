# we may use the functools imported into Python
from functools import reduce
# the reduce tool will keep applying the same function repeatedly

def addThem(n, m):
    '''return the sum of n+m'''
    return n+m

if __name__ == '__main__':
    v = range(0,11) # remember this is 0-10
    total = reduce(addThem, v)
    print(total)