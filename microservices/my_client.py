# a microservice client
import socket
import sys # we need this to access the system argument variables

def client():
    '''A microsevice client'''
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_tuple = ('localhost', 9876)
    client.connect(port_tuple)
    print(f'Client is running on {port_tuple[0]} port {port_tuple[1]}')
    # we may send a request to any server that is listening on this port
    # check if there are additional system arguments
    if len(sys.argv)>1:
        # all sys.argv members are string
        msg = ( ' '.join(sys.argv[1:]) ).encode()
    client.send(msg) # all communication must be encoded
    # when done, we tidy up
    client.close()

if __name__ == '__main__':
    client()