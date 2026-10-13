import sys

class RedircetOut():
    '''This class will redirect the standard output to a different output stream
    When complete, the original output stream will be restored'''
    def __init__(self, new_stream): # we can pass in teh target output stream (e.g. file writer)
        self.new_stream = new_stream
    def __enter__(self):
        '''swap the original stream for this new one (and stroe a reference to the original)'''
        self.old_stream = sys.stdout # remember what the current output stream is
        sys.stdout = self.new_stream # set the standard output to use our output stream
    def __exit__(self, exc_type, exc, tb):
        '''return the original output stream'''
        sys.stdout = self.old_stream

if __name__ == '__main__':
    # sys exposes some standard streams
    # print( sys.stdout ) # a standard output stream: (over)write UTF-8
    # print( sys.stdin )  # a standard input stream: read UTF-8
    # print( sys.stderr )
    with open('my_log.txt', 'at') as fout: # here we will append to a text file
        r = RedircetOut(fout) # send our output stream to the class __init__ method
        with r:
            print('This content will be redirected by the __enter__ method')
        # the __exit__ method should return the standrad output to be the console
        print('what about this?')