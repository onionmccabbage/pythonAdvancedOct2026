# using the asyncio library to build a client
import asyncio
import sys

# NB there is no absolute reason for any client to be asynchronous
# Howver in mucroservices they often need to be
async def myClient(message='default'):
    reader, writer = await asyncio.open_connection('localhost', 9876)
    print('sending a message')
    writer.write(message.encode())
    await writer.drain() # wait for teh message stream to exhaust
    writer.close()

if __name__ == '__main__':
    if len(sys.argv)>1:
        msg = ' '.join(sys.argv[1:])
    else:
        msg = 'hello'
    asyncio.run( myClient(msg) )