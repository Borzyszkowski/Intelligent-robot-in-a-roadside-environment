""" Intelligent robot in a roadside environment - client code for keyboard streaming in TCP/IP socket connection """

__author__ = 'Borzyszkowski'

import serial
from socket import *
import time


def typing():
    prediction = input("Type F,B,R,L or S: ")
    prediction = str(prediction)
    prediction = prediction.lower()
    print(prediction)
    return prediction


def streaming(host, port):
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        print("Host IP: ", host)
        print("Streaming keyboard buttons to server...")

        while True:
            # prediction='s'
            prediction = typing()
            client_socket.sendall(prediction.encode('utf-8'))
            time.sleep(0.01)
    finally:
        self.connection.close()
        self.server_socket.close()


if __name__ == '__main__':
    h = '172.20.10.2'
    p = 65531
    streaming(h, p)
