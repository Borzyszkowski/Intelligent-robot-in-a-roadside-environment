from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180
camera.start_preview()

camera.start_recording('./Recorded/video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()
