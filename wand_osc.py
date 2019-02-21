# requires the following python libraries:
#  python-osc
#  pyserial

import serial
from pythonosc import udp_client

# change this string depending upon where your computer makes a device for the micro:bit
serialport = "/dev/cu.usbmodem1412"

ser = serial.Serial(serialport, 115200)
client = udp_client.SimpleUDPClient("localhost", 8999)

while(True):
    line = ser.readline().decode('utf8').strip()

    x, y, z = map(float, line.split("^"))

    print(f"({x}, {y}, {z})")

    client.send_message("/wand_accel", [x, y, z] )
