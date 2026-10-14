# using the asyncio library to build a socket server
import asyncio

# when working with asynchronous code, we must mark our functions as 'async'
# This lets the function wait for a resposne
# Any response is marked with 'await' to indicate it might take some time

async def handleRequests(reader, writer):
    '''This async server will handle client requests'''
    data = await reader.read(1024) # all the underlying config is abstracted away
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print(f'Server received {message} from {addr}')
    # we could act conditionally based on the request content
    if message == b'Neo':
        print('We\'ve been waiting...')


async def main():
    server = await asyncio.start_server(handleRequests, 'localhost', 9876)
    print('Server started')
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run( main() ) # this is how we invoke asynchronous operations