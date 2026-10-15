# We may create our own decorator function
# Decorators may be applied to any other function

# all decorators add additional functionality 
def showArgs(f):
    '''This function will be used to decorate other functions
    Its purpose will be to reveal all the arguments (args and kwargs) of a function'''
    def newFn(*args, **kwargs):
        print(f'Running a function called {f.__name__}')
        print(f'The positional arguments tuple is {args}')
        print(f'The keyword argunents dict is {kwargs}')
        # we must return the result of calling the orginal function
        return f(*args, **kwargs)
    return newFn # return our new function without calling it

@showArgs # our decorator is now applied to the function
def isOdd(n):
    return n%2 == 1

# we may accept both keyword and positional arguments
@showArgs
def fnC(g, h, j, k=True, l=(1,2,3,4)): # obviously every argument may take ANY data type
    '''Rule: all positional arguments must come before any keyword arguments'''
    pass

if __name__ == '__main__':
    '''call a standard function (that has our decorator applied)'''
    r = isOdd(3)
    print(r)
    fnC(True, [], 'done', l=(6,5,4,3))
