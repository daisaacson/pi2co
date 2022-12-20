from machine import Pin
import time

onBoardLed = Pin(25, Pin.OUT)
unit = 0.15
morseDot = unit
morseDash = unit*3
morseLetter = unit
morseWord = unit*7
morseCode = {
    "A": [0,1],
    "B": [1,0,0,0],
    "C": [1,0,1,0],
    "D": [1,0,0],
    "E": [0],
    "F": [0,0,1,0],
    "G": [1,1,0],
    "H": [0,0,0,0],
    "I": [0,0],
    "J": [0,1,1,1],
    "K": [1,0,1],
    "L": [0,1,0,0],
    "M": [1,1],
    "N": [1,0],
    "O": [0,0,0],
    "P": [0,1,1,0],
    "Q": [1,1,0,1],
    "R": [0,1,0],
    "S": [1,1,1],
    "T": [1],
    "U": [0,0,1],
    "V": [0,0,0,1],
    "W": [0,1,1],
    "X": [1,0,0,1],
    "Y": [1,0,1,1],
    "Z": [1,1,0,0],
    "0": [1,1,1,1,1],
    "1": [0,1,1,1,1],
    "2": [0,0,1,1,1],
    "3": [0,0,0,1,1],
    "4": [0,0,0,0,1],
    "5": [0,0,0,0,0],
    "6": [1,0,0,0,0],
    "7": [1,1,0,0,0],
    "8": [1,1,1,0,0],
    "9": [1,1,1,1,0]
}

message = "The quick brown fox jumps over the lazy dog"

def morse_blink(letter, led):
    for code in letter:
        # turn led on
        led.value(1)
        # sleep appropriate time
        if code == 0:
            time.sleep(morseDot)
        if code == 1:
            time.sleep(morseDash)
        # turn led off
        led.value(0)
        # sleep intra-character
        time.sleep(morseLetter)
    # letter is done, sleep longer inter-character
    time.sleep(morseLetter*2)

def send_morse(message, led):
    # turn off led and sleep
    led.value(0)
    time.sleep(morseWord*2)
    
    # parse message
    for letter in message.upper():
        if letter in morseCode:
            morse_blink(morseCode[letter],led)
        else:
            # sleep word space
            time.sleep(morseWord)
            
while True:
    send_morse(message, onBoardLed)
