import serial
import math
from pythonosc import udp_client
from pythonosc import osc_message_builder
#port - /dev/cu.usbmodem1412


PORT = "/dev/cu.usbmodem1412"

BAUD = 115200

s = serial.Serial(PORT)

s.baudrate = BAUD

s.parity = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE



send_address = '127.0.0.1', 6448

# OSC basic client
c = udp_client.SimpleUDPClient('127.00.1', 6448)

try:
	while True:
		data = str(s.readline().rstrip())
		x_y_z = data[2:].split(" ")
		#data = float(data)
		x = int(x_y_z[0])
		y = int(x_y_z[1])
		strength = math.sqrt(x**2+y**2)
		c.send_message("/wek/inputs", strength)
		print(strength)

finally:
	s.close()