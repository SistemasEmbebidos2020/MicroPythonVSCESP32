from machine import Pin
from utime import sleep

p2 = Pin(25, Pin.OUT)
#p2.on()
print("Hola mundo Esp32,Python")
t = 0
while(t < 3):
    p2.on()
    print("On")
    sleep(2)
    p2.off()
    print("Off")
    sleep(1)
    t+=1
