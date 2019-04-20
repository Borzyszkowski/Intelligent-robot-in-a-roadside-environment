""" Intelligent robot in a roadside environment - server code for keyboard streaming in TCP/IP socket connection """

__author__ = 'Borzyszkowski'

import socket
import time
import explorerhat


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

            explorerhat.light.yellow.on()
            explorerhat.light.blue.on()

            prev = ''
            while True:
                prediction = self.connection.recv(1)
                prediction = prediction.decode('utf_8')
                print(prediction)
                print(prev)
                self.steer(prediction, prev)
                time.sleep(0.01)  # send data to the server every 0.01 sec
                if (prev == 'w' or prev == 's') and prediction != 'w' and prediction != 's':
                    prev += prediction
                elif (prev == 'wa' or prev == 'wd') and prediction != 'w' and prediction != 's':
                    prev = 'w' + prediction
                elif (prev == 'sa' or prev == 'sd') and prediction != 's' and prediction != 'w':
                    prev = 's' + prediction
                else:
                    prev = prediction
        finally:
            self.server_socket.close()

    @staticmethod
    def steer(prediction, prev):
        if prediction == 'w':
            if prev != 'w' and prev != 'wd' and prev != 'wa':
                explorerhat.motor.stop()
                time.sleep(0.5)  # give 0.5 sec for healthy engines
            explorerhat.motor.forwards()
            explorerhat.light.green.on()
            explorerhat.light.yellow.off()
            explorerhat.light.blue.off()
            explorerhat.light.red.off()
            print("Forward")

        elif prediction == 's':
            if prev != 's' and prev != 'sd' and prev != 'sa':
                explorerhat.motor.stop()
                time.sleep(0.5)  # give 0.5 sec for healthy engines
            explorerhat.motor.backwards()
            explorerhat.light.green.off()
            explorerhat.light.yellow.off()
            explorerhat.light.blue.on()
            explorerhat.light.red.off()
            print("Backward")

        elif prediction == 'd':
            if prev == 'w' or prev == 'wa' or prev == 'wd':
                explorerhat.motor.one.speed(100)
                explorerhat.motor.two.speed(20)
            elif prev == 's' or prev == 'sa' or prev == 'sd':
                explorerhat.motor.one.speed(-100)
                explorerhat.motor.two.speed(-20)
            else:
                explorerhat.motor.stop()
            explorerhat.light.yellow.on()
            explorerhat.light.red.off()
            print("Left")

        elif prediction == 'a':
            if prev == 'w' or prev == 'wd' or prev == 'wa':
                explorerhat.motor.one.speed(20)
                explorerhat.motor.two.speed(100)
            elif prev == 's' or prev == 'sd' or prev == 'sa':
                explorerhat.motor.one.speed(-20)
                explorerhat.motor.two.speed(-100)
            else:
                explorerhat.motor.stop()
            explorerhat.light.yellow.on()
            explorerhat.light.red.off()
            print("Right")

        elif prediction == 'z':
            explorerhat.motor.stop()
            explorerhat.light.green.off()
            explorerhat.light.yellow.off()
            explorerhat.light.blue.off()
            explorerhat.light.red.on()
            print("Stop")

        elif prediction == 'e':
            explorerhat.motor.stop()
            time.sleep(0.5)  # give 0.5 sec for healthy engines
            explorerhat.motor.one.forwards()
            explorerhat.motor.two.backwards()
            explorerhat.light.green.off()
            explorerhat.light.yellow.on()
            explorerhat.light.blue.off()
            explorerhat.light.red.off()
            print("Left - in place")

        elif prediction == 'q':
            explorerhat.motor.stop()
            time.sleep(0.5)  # give 0.5 sec for healthy engines
            explorerhat.motor.one.backwards()
            explorerhat.motor.two.forwards()
            explorerhat.light.green.off()
            explorerhat.light.yellow.on()
            explorerhat.light.blue.off()
            explorerhat.light.red.off()
            print("Right - in place")

        else:
            print("Character not recognized")


def choose_button(channel, event):
    if channel == 2:
        server_launch()
    elif channel == 1:
        print("2: Computer control")
    elif channel == 3:
        print("3: Autonomous drive")


def server_launch():
    h = '172.20.10.2'
    p = 65531
    print("Server is waiting for clients.")
    explorerhat.light.green.on()
    explorerhat.light.red.on()
    explorerhat.light.yellow.off()
    KeyboardStreaming(h, p)


if __name__ == '__main__':
    print("Press the button:")
    print("1: Button control")
    print("2: Computer control")
    print("3: Autonomous drive")
    explorerhat.light.yellow.on()
    explorerhat.touch.pressed(choose_button)
