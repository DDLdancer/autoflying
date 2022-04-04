import RPi.GPIO as GPIO
import time

servoPIN_0 = 17
servoPIN_2 = 27

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN_0, GPIO.OUT)
GPIO.setup(servoPIN_2, GPIO.OUT)

GPIO_0 = GPIO.PWM(servoPIN_0, 50) # GPIO 17 for PWM with 50Hz
GPIO_2 = GPIO.PWM(servoPIN_2, 50) # GPIO 17 for PWM with 50Hz

GPIO_0.start(2.5) # Initialization
GPIO_2.start(7.5)

try:
  while True:
    GPIO_0.ChangeDutyCycle(5)
    GPIO_2.ChangeDutyCycle(5)
    time.sleep(0.5)
    GPIO_0.ChangeDutyCycle(7.5)
    GPIO_2.ChangeDutyCycle(2.5)
    #time.sleep(0.5)
    #p.ChangeDutyCycle(10)
    #time.sleep(0.5)
    #p.ChangeDutyCycle(12.5)
    #time.sleep(0.5)
    #p.ChangeDutyCycle(10)
    #time.sleep(0.5)
    #p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    GPIO_0.ChangeDutyCycle(5)
    GPIO_2.ChangeDutyCycle(5)
    time.sleep(0.5)
    GPIO_0.ChangeDutyCycle(2.5)
    GPIO_2.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    print("rotating")
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
