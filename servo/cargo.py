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

def up():
    GPIO_0.ChangeDutyCycle(5)
    GPIO_2.ChangeDutyCycle(5)
    time.sleep(0.5)
    GPIO_0.ChangeDutyCycle(7.5)
    GPIO_2.ChangeDutyCycle(2.5)
    time.sleep(0.5)

def down():
    GPIO_0.ChangeDutyCycle(5)
    GPIO_2.ChangeDutyCycle(5)
    time.sleep(0.5)
    GPIO_0.ChangeDutyCycle(2.5)
    GPIO_2.ChangeDutyCycle(7.5)
    time.sleep(0.5)

try:
  while True:
      down()
      input("Press enter to close")
      up()
      input("Press enter to open")

except KeyboardInterrupt:
    print("\nCleaning up...")
    GPIO_0.stop()
    GPIO_2.stop()
    GPIO.cleanup()
