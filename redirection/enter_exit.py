class ShowStuff():
    '''There are many features of Python which we may override with our own code
    They always look like this: __nnnn__ (dunder)
    e.g. __str__, __repr__, __init__, __main__ and many more'''
    def __init__(self):
        '''the __init__ method is run ONCE when an instance is created'''
        print('inside the __init__ method')
    def __enter__(self):
        '''the __enter__ method is invoked every time we start using an instance'''
        print('inside the __enter__ method')

    # CAREFUL - when we override __exit__ we MUST allow for all the arguments
    def __exit__(self, exc_type, exc, tb):
        print(f'inside the __exit__ method. {exc_type}, {exc}, {tb}')

if __name__ == '__main__':
    r = ShowStuff() # this will invoke the __init__ method
    with r:
        print('r is in use')
        print('more use of r')
        # when the 'with' ends, this instance is no longer being used
    with r:
        print('r is in use')
        print('more use of r')
        # when the 'with' ends, this instance is no longer being used