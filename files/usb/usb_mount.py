#!/usr/bin/env python
# -*- coding: utf-8 -*-

# quick usb mounter using udiskie-mount
# Copyright (C) 2017 Samuel Walladge
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os
import re
import subprocess
import argparse

parser = argparse.ArgumentParser(description='USB drive mount/unmount with udiskie.')
parser.add_argument('--unmount', '-u', action='store_true', default=False,
                    help='unmount a drive instead of mount')

args = parser.parse_args()

# EDIT THIS TO SUIT YOUR SETUP
# ignores sda and sdb on my machine since they are internal drives
RE_match = re.compile(r'sd[c-z]\d+')
def is_mountable(dir_name):
    return RE_match.match(dir_name) is not None

  
print('Choose drive to ' + ('un' if args.unmount else '') + 'mount.')

dirs = list(filter(is_mountable, os.listdir('/dev/')))

for i, d in enumerate(dirs):
    print('[{}] /dev/{}'.format(i, d))

while True:
    choice = input('Enter number [0]: ')
    try:
        if not choice.strip():
            choice = 0
        choice = int(choice)
        if choice >= len(dirs) or choice < 0:
            raise ValueError('number out of bounds')
        break
    except Exception as e:
        print(e.args[0])

subprocess.run(['udiskie-' + ('u' if args.unmount else '') + 'mount', '/dev/' + dirs[choice-1]])
