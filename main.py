#!/usr/bin/env python

import spidev
import time
import subprocess

# open spi devices
spi = spidev.SpiDev()
spi.open(0, 0)

try:
    while True:
        res = spi.xfer2([0x68, 0x00])
        value = (res[0] * 256 + res[1]) & 0x3ff
        print value
        time.sleep(1)   #sleep 1sec
except KeyboardInterrupt:
    spi.close()
