#!/usr/bin/env python

import pefile
import sys
import os

if len(sys.argv)<2:
	print "Usage: %s <binary>" % sys.argv[0]
	sys.exit()

filename=sys.argv[1]

if not os.path.isfile(filename):
	print "File not found..."
	sys.exit()

pe =  pefile.PE(filename, fast_load=True)

for section in pe.sections:
  print (section.Name, hex(section.VirtualAddress),
    hex(section.Misc_VirtualSize), section.SizeOfRawData )
