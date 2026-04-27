import machine
import time

TRIG = machine.Pin(16, machine.Pin.OUT)
ECHO = machine.Pin(17, machine.Pin.IN)

def distance():
    time.sleep_ms(50) #stabilize the sensor
    
    TRIG.value(0)
    time.sleep_us(2)
    TRIG.value(1)
    time.sleep_us(10)
    TRIG.value(0)

    timeout = 30000
    start = time.ticks_us()

    while ECHO.value() == 0:
        if time.ticks_diff(time.ticks_us(), start) > timeout:
            return None
        time.sleep_us(1)

    time1 = time.ticks_us()
    start = time.ticks_us()

    while ECHO.value() == 1:
        if time.ticks_diff(time.ticks_us(), start) > timeout:
            return None
        time.sleep_us(1)

    time2 = time.ticks_us()

    return (time.ticks_diff(time2, time1) * 0.0343) / 2

while True:
    d = distance()
    print("Distance:", d)
    time.sleep_ms(500)