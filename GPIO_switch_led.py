import RPi.GPIO as GPIO
from time import sleep, strftime
from datetime import datetime

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT
Switch= 10
LED = 3

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

# Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)


def main():
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, width=8, height=8, block_orientation=0)
    print(device)
    device.contrast(100)
    virtual = viewport(device, width=8, height=8)
    Flag =0
    
    #show_message(device, 'Raspberry Pi MAX7219', fill="white", font=proportional(LCD_FONT), scroll_delay=0.08)

    while True:
        if (GPIO.input(Switch) == GPIO.HIGH and Flag==0):
           GPIO.output(LED, GPIO.HIGH)
           Flag = 1
       
 

           print("Button was pushed!")
           with canvas(virtual) as draw:
               text(draw, (0, 1), 'O', fill="white", font=proportional(CP437_FONT))

        
        elif(GPIO.input(Switch) == GPIO.HIGH and Flag==1):
            Flag = 0
            print("Button was not pushed!")
            GPIO.output(LED, GPIO.LOW)
            with canvas(virtual) as draw:
                text(draw, (0, 1), 'X', fill="white", font=proportional(CP437_FONT))
        sleep(2)
        

'''
        for _ in range(1):
            for intensity in range(16):
                device.contrast(intensity*16)
                sleep(0.1)
'''

if __name__ == '__main__':
    main()
