# -*- coding: utf-8 -*-
"""
Description:
Checks for USB device, if found,
Moves the specified file to the new specified path
"""

import sys, os, shutil
from glob import glob

class usbClass:
	#path1 = "/home/pi/Pictures/4.jpg"									# RasPi - path to timelapse directory
	path1 = "/home/antz/Pictures/4.jpg"									# PC - path to timelapse directory
	#path2 = "/media/pi/"												# RasPi - path to media
	#path2 = "/media/antz/"												# PC - path to media
	#path3 = "/media/pi/flash_name/"									# path to usb destination

	def __init__(self, **kwargs):
		print("USB Class initialised!")

	def usb_put(self, path2):
		#path2 = "/media/pi/"										# RasPi - path to media
		#path2 = "/media/antz/"										# PC - path to media
		try:
			path2 = glob(path2 + "*/")								# returns as list item
			print(path2[0])											# must ref item[0]
				
			## Check for USB destination path ##
			directory = os.path.dirname(path2[0])					# check in images file path
			if not os.path.exists(directory):						# if directory doesn't exist
				print("Directory doesn't exist!")					# Notify if directory was created
			else:
				print("path exists")
				try:												# [Skip if file doesn't exist]
					# Copy file to new destination
					src = self.path1
					dst = path2[0]
					# move the file
					shutil.move(src, dst)
					print("Move complete!")
					#sys.exit(0)									# calls exception every time???
					print("exit")
				except:
					print("No file to copy...")						# Notify user
					sys.exit(0)										# exit properly 
		except:
			print("No USB Device!")
