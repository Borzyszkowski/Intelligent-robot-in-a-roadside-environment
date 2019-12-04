<p align="center"><img src="https://www.sbcar.eu/wp-content/uploads/2018/05/Gdansk-University-of-Technology-loggo.png" width="300" align="middle"></p>

<br>

# Intelligent robot in a roadside environment
Intelligent robot in a roadside environment accelerated by Intel Movidius Neural Compute Stick.

Project of Gdańsk University of Technology in collaboration with Karunya Insititute of Technology and Sciences.

## Overview

Nowadays, intelligent technologies gained on popularity both in software and hardware development, finding innovative applications in numerous branches of industry. Following the needs of complex computations in neural networks, a wide range of processors dedicated for artificial intelligence purposes has been released. Due to massive consumption of energy and time during the training of deep neural networks, production of efficient AI chips for embedded systems is especially demanding. Although the limitations, this is a crucial field of research which can be an opportunity for groundbreaking results in various domains, such as a vehicle production. 

In this project we design a model of an intelligent robot based on Raspberry Pi and present its different capabilities under certain conditions of a roadside environment which we likewise construct. We propose various possibilities of control over the robot, including a remote steering from the client computer through the TCP/IP transmission. Finally, we investigate a utilization of Intel Movidius Neural Compute Stick and use OpenVINO toolkit to deploy a deep neural network for characterization of road signs from the level of embedded platform. As a result of a long term collaboration on this topic we present a complete project of a smart vehicle having multiple functions inspired by the actual traffic flow.

<br>

<p align="center"><img src="https://imgur.com/w9fNPhL.jpg" width="600" align="middle"></p>

<br>

### How to run?
>~~~~
>git clone https://github.com/Borzyszkowski/Intelligent-robot-in-a-roadside-environment.git
>~~~~

##### Raspberry Pi (robot):
>~~~~
>python server_keyboard_raspberry.py
>python server_video_raspberry.py
>~~~~

##### Computer (user):
>~~~~
>python client_keyboard_pc.py
>python client_video_pc.py
>~~~~


### Useful links

* Learn more about [Intel Movidius Neural Compute Stick](https://software.intel.com/en-us/movidius-ncs).
* [OpenVINO toolkit overview](https://software.intel.com/en-us/openvino-toolkit) - Development of applications and solutions that emulate human vision
