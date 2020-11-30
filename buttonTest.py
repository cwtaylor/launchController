import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


goButtonPin = 2
switchPin = 3
emergencyButton = 4

GPIO.setup(switchPin, GPIO.IN)
GPIO.setup(goButtonPin, GPIO.IN)


try:
  def pressed(channel):
    armed = GPIO.input(switchPin)
    if armed == GPIO.LOW:
      print("Go Go Go!")
      rfm9x.send(bytes("Go Go Go!\r\n", "utf-8"))

    else:   
      print("Pressed without arming!")


  GPIO.add_event_detect(goButtonPin, GPIO.RISING, callback=pressed)
  
finally:
  GPIO.cleanup()
