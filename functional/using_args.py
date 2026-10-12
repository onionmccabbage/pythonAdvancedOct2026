# Every function (and every method in a class) may take 
# positional arguments and also keyword arguments

# here is a function taking only positional arguments
def fnA(x, y, z): # the arguments are in an ordinal position, 0, 1, 2...
    pass

# this function takes only keyword arguments
def fnB(m=1, n=2): # we may also think of these as arguments with default values
    pass

# we may accept both keyword and positional arguments
def fnC(g, h, j, k=True, l=(1,2,3,4)): # obviously every argument may take ANY data type
    '''Rule: all positional arguments must come before any keyword arguments'''
    pass

# These ideas may be used as 'args' and 'kwargs' like this
def fnD(*args): # in all function, every positional argument is gathered into a tuple
    print( args, type(args) )

def fnE(**kwargs): # in all functions, every keyword-argument is gathered into a dict
    print( kwargs, type(kwargs) )

# we may use this to behave differently dpending on the number of arguments
def runTests( *args, **kwargs ):
    '''if there are arguments, use them as tests
    For any kwargs, use them as controllers'''
    if len(args)>0:
        for _ in args:
            print(f'Running test for {_}')
    for (k, v) in kwargs.items():
        print(f'Controlling {k} with {v}')

if __name__ == '__main__':
    '''exercise our code'''
    fnA('position zero', 'position one', 'position two')
    fnB(n=3, m=4) # the position does not matter
    fnC([4,3,2], {'n':'one', 'm':'two'}, {5,6,7,8}  ) # here 'l' will be the default value
    # making use of args and kwargs
    fnD() # no positional arguments
    fnD(1,3,8) # some positional arguments
    fnD([3,2,1], (1,), {5,4,True}, fnA)
    # using kwargs
    fnE( h=False, j=fnD, zzz='plural alpha', ww={5,3,-1} )
    fnE() # no arguemtns whatsoever!

    # simulate our test runner function
    runTests(4, 6, 2, -11, jvalue=True, useDate=False, outputTarget='DB')
  
