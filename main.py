#!/usr/bin/python

import spidev
import time
import subprocess

# open spi devices
spi_left = spidev.SpiDev()
spi_right= spidev.SpiDev()

spi_left.open(0, 0)
spi_right.open(0, 1)

count = 0

try:
    while True:
        res_left = spi_left.xfer2([0x68, 0x00])
        value_left = (res_left[0] * 256 + res_left[1]) & 0x3ff
        print "left: " + str(value_left)
	# if value_left > 500:
#		count += 1
	# print count	
        res_right = spi_right.xfer2([0x68, 0x00])
        value_right = (res_right[0] * 256 + res_right[1]) & 0x3ff
        print "right: " + str(value_right)
        time.sleep(0.1)   #sleep 1sec
except KeyboardInterrupt:
    spi_left.close()
    spi_right.close()
