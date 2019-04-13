""" Intelligent robot in a roadside environment - server code for video streaming in TCP/IP socket connection """

__author__ = 'Borzyszkowski'

import io
import socket
import struct
import time
import picamera


class VideoStreamingTest(object):
    def __init__(self, host, port):
        self.server_socket = socket.socket()
        self.server_socket.bind((host, port))
        self.server_socket.listen(0)
        self.connection, self.client_address = self.server_socket.accept()
        self.connection = self.connection.makefile('wb')
        self.host_name = socket.gethostname()
        self.host_ip = socket.gethostbyname(self.host_name)
        self.streaming()

    def streaming(self):
        try:

            print("Host: ", self.host_name + ' ' + self.host_ip)
            print("Connection from client: ", self.client_address)
            print("Streaming...")

            with picamera.PiCamera() as camera:
                camera.resolution = (640, 480)  # pi camera resolution
                camera.rotation = 180
                camera.framerate = 20  # 20 frames/sec
                time.sleep(2)  # give 2 secs for camera to initialize
                start = time.time()
                stream = io.BytesIO()

                # send jpeg format video stream
                for foo in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
                    self.connection.write(struct.pack('<L', stream.tell()))
                    self.connection.flush()
                    stream.seek(0)
                    self.connection.write(stream.read())
                    if time.time() - start > 600:
                        break
                    stream.seek(0)
                    stream.truncate()
            self.connection.write(struct.pack('<L', 0))

        finally:
            print("Connection finished by user")
            self.connection.close()
            self.server_socket.close()


if __name__ == '__main__':
    h = '172.20.10.2'
    p = 65532
    VideoStreamingTest(h, p)

