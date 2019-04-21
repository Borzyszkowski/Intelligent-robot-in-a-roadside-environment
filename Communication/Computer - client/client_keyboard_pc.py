""" Intelligent robot in a roadside environment - client code for keyboard streaming in TCP/IP socket connection """

__author__ = 'Borzyszkowski'

import msvcrt
from socket import *
import time


def typing():
    # prediction = str(input()).lower()
    prediction = str(msvcrt.getch()).lower()
    prediction = prediction[-2]
    print(prediction)
    return prediction


def streaming(host, port):
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        print("Host IP: ", host)
        print("Streaming keyboard buttons to server...")

        print("Control the robot. Type:")
        print("W - forward")
        print("S - backward")
        print("A - left forward/backward")
        print("D - right forward/backward")
        print("Z - stop")
        print("Q - left in place")
        print("E - right in place")
        while True:
            # prediction='s'
            prediction = typing()
            client_socket.sendall(prediction.encode('utf-8'))
            time.sleep(0.01)
    finally:
        return


if __name__ == '__main__':
    h = '172.20.10.2'
    p = 65531
    streaming(h, p)
