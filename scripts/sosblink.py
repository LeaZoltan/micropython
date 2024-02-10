#written by Lea 1/20
#this file makes pico's LED blink for one second

from include.rcc_library import Raft
import utime

myraft = Raft()

myraft.led_on()
utime.sleep_ms(1000)
myraft.led_off()