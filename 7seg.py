from machine import Pin
import utime
def show(digito, display):
    anodo = (int('40',16),int('79',16),int('24',16),int('30',16),int('19',16),int('12',16),int('02',16),int('78',16),int('00',16),int('18',16))
    bit = 1;    
    for i in range(7):
        if (anodo[digito]  & bit) == 0:
            display[i].off()
        else:
            display[i].on()
        bit = bit << 1
    
while True:
    display_pins = (22, 23, 15, 2, 4, 21, 19) 
    display = list()
    for i in range(7):
        display.append( Pin( display_pins[i], Pin.OUT ) )
    contador = 0
    sentido = True
    while True:
        show(contador, display)
        
        if sentido:
            contador += 1
        else:
            contador -= 1

        if contador == 9:
            sentido = False
        
        if contador == 0:
            sentido = True
        
        utime.sleep(1)
    
