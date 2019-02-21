from pythonosc import dispatcher
from pythonosc import osc_server
import math

bird_speeds = [0]

def calculate_throw(unused_addr, args, num1, num2):
	bird_speed = int(num1*100)
	bird_angle = int(abs(num2*90))
	bird_speeds.append(bird_speed)
	if(bird_speeds[1] > bird_speeds[0]+10):
		print("Your bird traveled",bird_speed,"feet at a ", bird_angle, " percent optimal launch angle")
	del bird_speeds[1]
	#sp = args[1]
try:
	while True:
		dispatcher = dispatcher.Dispatcher()
		dispatcher.map("/wek/outputs", calculate_throw, "bird speed", "bird_angle")

		server = osc_server.ThreadingOSCUDPServer( ("127.0.0.1", 12000), dispatcher)

		server.serve_forever()
except KeyboardInterrupt:
	print("\nsClient Ctrl-C\nShutting Down Server")
