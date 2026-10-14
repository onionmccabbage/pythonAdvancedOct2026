# a microservice server
import socket

def server():
    '''This microservice will listen for requests and respond'''
    # here are some sensible settings for socket communication
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_tuple = ('localhost', 9876)
    server.bind(port_tuple) # our server now has a port over IP4
    print(f'Server is running on {port_tuple[0]} port {port_tuple[1]}')
    # we need to begin listening for client requests
    server.listen() # we may set a backlog, controlling concurrent client handling 
    while True: # this is an endless loop (a run-loop)
        # accept any request from clients
        (client, addr) = server.accept()
        print(f'Server received a request from {addr}')
        buf = client.recv(1024) # only receive the first 1024 bytes
        # we may choose how to proceed based on this initial buffer of data
        print(f'Server received {buf}') # NB the buffer is url-encoded
        if buf == b'quit':
            break # this will end the while loop

if __name__ == '__main__':
    server() # invoke the server
