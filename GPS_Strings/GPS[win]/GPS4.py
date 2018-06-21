# -*- coding: utf-8 -*-
"""
Created by: 	A.Smith
Date:			2017-08-08
Description:	USB-Serial comms to uBlox NEO-M8T-Q-10
				Remove all other GPS NMEA string except $GPRMS
"""
import serial
from time import sleep

port = "COM11"
baud = 19200

coord = []
list = ["$PUBX,40,GGA,0,0,0,0*5A",
		"$PUBX,40,GLL,0,0,0,0*5C",
		"$PUBX,40,VTG,0,0,0,0*5E",
		"$PUBX,40,GSV,0,0,0,0*59",
		"$PUBX,40,GSA,0,0,0,0*4E",
		"$PUBX,40,ZDA,0,0,0,0*44"]

def main():
	count = 0
	pos = 0
	ser = serial.Serial(port, baud, timeout=1)
	# open the serial port
	if ser.isOpen():
		print(ser.name + ' is open...')
	
	# Eliminate other messages
	for rms in list:
		cmd = rms								# Get command 
		ser.write(cmd.encode('ascii')+'\r\n')	# convert to ASCII
		out = ser.read()						# output to GPS
		sleep(0.005)							# delay 5ms

	while True:
		out = ser.read()
		#print(out),
		coord.append(sender)					# Copy char to string array
		#coord[pos] = out 						# Copy char to string array
		pos += 1 								# increment position
		
		if out == '*':
			pos = 0 							# clear position counter
			if count == 10:
				count = 0						# reset exit counter
				cmd = raw_input("\nEnter command or 'exit':")
				if cmd == 'exit':
					ser.close()					# close the serial connection
					exit()						# exit -> sys.exit(0)
				else:
					#print(coord),				# print the string?
					for j in range(0,len(coords)):
						print(coords[j]),		# print each character
			else:
				count += 1

if __name__ == '__main__': main()