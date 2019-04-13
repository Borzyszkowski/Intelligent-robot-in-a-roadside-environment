""" Intelligent robot in a roadside environment - client code for TCP/IP socket connection """

__author__ = 'Borzyszkowski'

import numpy as np
import cv2
import socket


def streaming(host, port):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    connection = client_socket.makefile('wb')

    try:
        print("Host IP: ", host)
        print("Streaming video from server...")
        print("Press 'q' to exit")

        stream_bytes = b' '
        while True:
            stream_bytes += client_socket.recv(1024)
            first = stream_bytes.find(b'\xff\xd8')
            last = stream_bytes.find(b'\xff\xd9')
            if first != -1 and last != -1:
                jpg = stream_bytes[first:last + 2]
                stream_bytes = stream_bytes[last + 2:]
                image = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                cv2.imshow('Intelligent robot in a roadside environment', image)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("Connection finished by user")
                    return
    finally:
        connection.close()
        client_socket.close()


if __name__ == '__main__':
    h = '172.20.10.2'
    p = 65532
    streaming(h, p)



