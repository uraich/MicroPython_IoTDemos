from machine import Pin,PWM
import time
p14=Pin(14)   # the buzzer runs from this pin
pwm14=PWM(p14)

pwm14.freq(500)
pwm14.duty(512)

time.sleep(1)
pwm14.deinit()
