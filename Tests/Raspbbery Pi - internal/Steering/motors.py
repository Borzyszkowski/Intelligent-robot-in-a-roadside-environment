""" Intelligent robot in a roadside environment - raspberry code for motor tests """

__author__ = 'Borzyszkowski'

import time
import explorerhat


print("Press CTRL+C to exit.")
explorerhat.motor.forwards()
touched = [False] * 8


def ohai(channel, event):
    touched[channel - 1] = True
    print("{}: {}".format(channel, event))


explorerhat.touch.pressed(ohai)
explorerhat.touch.released(ohai)

explorerhat.light[0].on()
explorerhat.light[2].on()

explorerhat.output[0].on()
explorerhat.output[2].on()

input_status = False

while True:

    if explorerhat.is_explorer_pro():
        print(explorerhat.analog.read())
    print(explorerhat.input.read())
    if sum(explorerhat.input.read().values()) == 4:
        input_status = True
    print('Input Status:', input_status)
    print('Touch Status:', sum(touched) == 8)

    if input_status and sum(touched) == 8:
        explorerhat.light.off()
        explorerhat.light.green.on()
    else:
        explorerhat.light.toggle()
    explorerhat.output.toggle()

    time.sleep(1)

explorerhat.pause()
