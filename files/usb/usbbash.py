# -*- coding: utf-8 -*-
"""
Description:
Uses "subprocess" to run "usbbash.sh" script
"""
# import the necessary packages
import subprocess

def main():
	subprocess.call("./usbbash.sh")
		
if __name__ == "__main__": main()
