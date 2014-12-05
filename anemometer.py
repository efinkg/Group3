#http://raspberry.io/projects/view/reading-from-a-mcp3002-analog-to-digital-converter/
from __future__ import division
import spidev
import time

def bitstring(n):
    s = bin(n)[2:]
    return '0'*(8-len(s)) + s

def read(adc_channel=0, spi_channel=0):
    conn = spidev.SpiDev(0, spi_channel)
    conn.max_speed_hz = 1200000 # 1.2 MHz
    conn.mode = 0
    #print "mode=", conn.mode
    cmd = 192
    if adc_channel:
        cmd += 32
    reply_bytes = conn.xfer2([cmd, 0])
    reply_bitstring = ''.join(bitstring(n) for n in reply_bytes)
    reply = reply_bitstring[5:15]
    return int((int(reply, 2)-125)/5)

if __name__ == '__main__':
   while True:
      print read()
