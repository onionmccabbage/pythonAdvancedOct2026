# we may need to operate with files which contain byte data (rather than plain text)
# every piece of data on a computer is ultimately 1 or 0 (a bit)
# when we have several bits together, that is a byte

def writeBytes(b): # we would be better off checking that b is actually bytes
    '''commit the byte data 'b' to a persistent (byte) file'''
    try:
        # we need a file system access object
        with open('my_bytes', 'ab') as fout: # 'ab' refers to append bytes
            fout.write(b)
            # when the with operator ends, it will automatically release resources
            # so there is no need to call fout.close()
    except Exception as err:
        print(err)

if __name__ == '__main__':
    myBytes = b'Here is a byte string' # the b makes this into bytes
    print(type(myBytes)) # we have bytes
    writeBytes(myBytes)  # call our function
    # other ways to create byte data
    c = bytes('wordy wordy word', 'UTF8')
    writeBytes(c)
    # iteratively create some byte data
    d = b''
    for _ in range(0, 256):
        d += bytes(_)
    print(d.decode()) # nb there is also an encode() method
    # send them to the byte file
    writeBytes(d)
