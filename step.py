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

def count():
        count = 0
        left_flag = False
	prev_value = 0
	while MAX_COUNT >= count:
		res_left = spi_left.xfer2([0x68, 0x00])
		value_left = (res_left[0] * 256 + res_left[1]) & 0x3ff
		res_right = spi_right.xfer2([0x68, 0x00])
		value_right = (res_right[0] * 256 + res_right[1]) & 0x3ff

		# print "left: " + str(value_left)
		if value_left - prev_value > THRESHOLD:
			count += 1
		        print count
		# print "right: " + str(value_right)
		prev_value = value_left
		time.sleep(0.1)   #sleep
