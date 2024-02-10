#written by Lea 1/20
#this file turns on pico's LED if conditions are met

from include.rcc_library import Raft

myraft = Raft()

favcolor = "blue"
age = 24

if favcolor == "blue" and age > 13:
    myraft.led_on()