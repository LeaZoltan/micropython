from include.rcc_library import Raft
import utime

myraft = Raft()

for i in range(5):
    myraft.led_on()
    utime.sleep_ms(100)
    myraft.led_off()
    utime.sleep_ms(1000)