# we may need to retrieve byte data
# NB many media files (byte files) declare their type early on in their bytes

def readBytes(whichFile='my_bytes'):
    '''Retreive bytes from a file'''
    try:
        with open(whichFile, 'rb') as fin: # 'rb' means read bytes
            b = fin.read() # also readline and readlines
            return b
    except Exception as err:
        print(err)

if __name__ == '__main__':
    # read our byte file
    retrieved = readBytes()
    print(retrieved.decode()) # may not be human readable
    # read Ericsson-Simbolo-650x366.png
    pic = readBytes('Ericsson-Simbolo-650x366.png')
    print(pic)