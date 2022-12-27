from machine import ADC
import time

temperatureBuffer = []
temperatureBufferLength = 60
temperatureFrequency = 10

temperatureSensor = machine.ADC(4)
conversionFactor = 3.3 / 65535


def toCelcius(raw):
    # convert raw temp sensor reading to Celcius
    return 27 - ((raw * conversionFactor) - 0.706)/0.001721

def toFahrenheit(raw):
    # convert raw temp sensor reading to Fahrenheit
    return 32 + ( 1.8 * toCelcius(raw) )

while True:
    # read raw temperature from sensor
    temperatureReadingRaw = temperatureSensor.read_u16()
    
    # Store raw vaules in a FIFO buffer to level out temperature readings
    temperatureBuffer.append(temperatureReadingRaw)
    if len(temperatureBuffer) > temperatureBufferLength:
        temperatureBuffer.pop(0)
        
    # Print averaged temperature reading
    print ("Temperature: {0:.1f}°F".format(toFahrenheit(sum(temperatureBuffer)/len(temperatureBuffer))))

    time.sleep(temperatureFrequency)
