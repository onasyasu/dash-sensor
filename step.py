#!/usr/bin/python

import spidev
import time
import subprocess

# open spi devices
spi_left = spidev.SpiDev()
spi_right= spidev.SpiDev()

spi_left.open(0, 0)
spi_right.open(0, 1)

MAX_COUNT = 10
THRESHOLD = 500
count = 0
left_flag = False

def count():
        count = 0
	while MAX_COUNT >= count:
		res_left = spi_left.xfer2([0x68, 0x00])
		value_left = (res_left[0] * 256 + res_left[1]) & 0x3ff
		res_right = spi_right.xfer2([0x68, 0x00])
		value_right = (res_right[0] * 256 + res_right[1]) & 0x3ff
                
		# print "left: " + str(value_left)
		if left_flag is False and value_left > value_right and value_left > THRESHOLD:
			left_flag = True
			count += 1
		elif left_flag is True and value_left < value_right and value_right > THRESHOLD:
			left_flag = False
			count += 1
		print count
		# print "right: " + str(value_right)
		time.sleep(0.1)   #sleep
