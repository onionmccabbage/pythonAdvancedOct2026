# redirection is such a useful idea it gets its own library, called context manager
from contextlib import contextmanager
import sys

@contextmanager # this decorator will let the function operate as a context-switcher
def outputRedirect(newOutput):
    '''this function will send any output to the new output stream
    All output defaults will be restored after operation'''
    old = sys.stdout
    sys.stdout = newOutput
    yield # this will yield a result without ending the function
    # restore
    sys.stdout = old
    # there is nothing left to do, so this function will end


if __name__ == '__main__':
    '''exercise the code'''
    with open('my_stream.txt', 'w') as fileObj:
        with outputRedirect(fileObj): # here we call our context manager function
            print('content to be redirected') # print always defaults to new-line
            sys.stdout.write('where does this go?') # no default new-line
    print('normal service is resumed')
    sys.stderr.write('oh no, this is a pretend error') # we may choose to redirect stderr 
