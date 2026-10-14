# a microservice client
import socket

def client():
    '''A microsevice client'''
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    