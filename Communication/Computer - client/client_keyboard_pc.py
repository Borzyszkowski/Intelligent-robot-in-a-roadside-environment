""" Intelligent robot in a roadside environment - client code for keyboard streaming in TCP/IP socket connection """

__author__ = 'Borzyszkowski'

import serial
from socket import *
import time


def typing():
    print("Control the robot. Type:")
    print("W - forward")
    print("S - backward")
    print("A - left forward/backward")
    print("D - right forward/backward")
    print("Z - stop")
    print("Q - left in place")
    print("E - right in place")
    prediction = str(input()).lower()
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
