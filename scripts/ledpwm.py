from machine import Pin, PWM

pin = 9 #number for gpio pin #pwm stands for pulse width modulation which is basically blinking

pwm_pin = PWM(Pin(pin))
#freuqnecy is cycles per seocnd (Herts, Hz)
pwm_pin.freq(10) #Hz

percent = 50

pwm_pin.duty_u16(percent*655)
