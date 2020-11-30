# Simple demo of sending and recieving data with the RFM95 LoRa radio.
# Author: Tony DiCola
import time
import board
import busio
import digitalio

import adafruit_rfm9x

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

CSPin = "D5"
resetPin = 6
goButtonPin = 2
switchPin = 3
emergencyButton = 4


# Define radio parameters.
RADIO_FREQ_MHZ = 915.0  # Frequency of the radio in Mhz. Must match your
# module! Can be a value like 915.0, 433.0, etc.

# Define pins connected to the chip, use these if wiring up the breakout according to the guide:
CS = digitalio.DigitalInOut(board.CSPin)
RESET = digitalio.DigitalInOut(board.resetPin)
# Or uncomment and instead use these if using a Feather M0 RFM9x board and the appropriate
# CircuitPython build:
# CS = digitalio.DigitalInOut(board.RFM9X_CS)
# RESET = digitalio.DigitalInOut(board.RFM9X_RST)

# Define the onboard LED
LED = digitalio.DigitalInOut(board.D13)
LED.direction = digitalio.Direction.OUTPUT

# Initialize SPI bus.
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Initialze RFM radio
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

# Note that the radio is configured in LoRa mode so you can't control sync
# word, encryption, frequency deviation, or other settings!

# You can however adjust the transmit power (in dB).  The default is 13 dB but
# high power radios like the RFM95 can go up to 23 dB:
rfm9x.tx_power = 23

# Send a packet.  Note you can only send a packet up to 252 bytes in length.
# This is a limitation of the radio packet size, so if you need to send larger
# amounts of data you will need to break it into smaller send calls.  Each send
# call will wait for the previous one to finish before continuing.

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

  
  
