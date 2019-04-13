""" Intelligent robot in a roadside environment - server code for keyboard streaming in TCP/IP socket connection """

__author__ = 'Borzyszkowski'

import socket
import time


class KeyboardStreaming(object):
    def __init__(self, host, port):

        self.server_socket = socket.socket()
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host, port))
        self.server_socket.listen(0)
        self.connection, self.client_address = self.server_socket.accept()
        self.host_name = socket.gethostname()
        self.host_ip = socket.gethostbyname(self.host_name)
        self.streaming()

    def streaming(self):

        try:
            print("Host: ", self.host_name + ' ' + self.host_ip)
            print("Connection from client: ", self.client_address)
            print("Streaming...")

            while True:
                prediction = self.connection.recv(1)
                prediction = prediction.decode('utf_8')
                print(prediction)
                self.steer(prediction)
                time.sleep(0.01)  # send data to the server every 0.01 sec
        finally:
            self.server_socket.close()

    @staticmethod
    def steer(prediction):
        if prediction == 'f':
            print("Forward")

        elif prediction == 'b':
            print("Backward")

        elif prediction == 'l':
            print("Left")

        elif prediction == 'r':
            print("Right")

        elif prediction == 's':
            print("Stop")

        else:
            print("Character not recognized")


if __name__ == '__main__':
    h = '172.20.10.2'
    p = 65531
    KeyboardStreaming(h, p)
