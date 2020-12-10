# 応用演習(PC)第１２回授業内に作成
# 2020/12/10

from time import sleep
from gpiozero import LED
import RPi.GPIO as GPIO
import time

relay_pin = 17
LED(relay_pin, active_high=False)

def main_loop():
    while True:
        GPIO.output(relay_pin, 0)
        sleep(0.5)
        GPIO.output(relay_pin, 1)
        sleep(0.5)


if __name__ == "__main__":
    main_loop()
