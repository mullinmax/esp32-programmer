import time
import math
import machine, neopixel

import config
import sys
import random
import network
# import urequests

def connect_to_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(config.wifi['ssid'], config.wifi['password'])
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

# def wget(url):
#     response = urequests.get(url)
#     response.json()

def lerp(start, stop, percent):
    return start + (stop-start) * percent

def pix_lerp(start, stop, percent):
    out = (
        int(lerp(start[0],stop[0],percent)),
        int(lerp(start[1],stop[1],percent)),
        int(lerp(start[2],stop[2],percent))
    )
    return out

def random_color():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def say(s=None):
    if s is None:
        sys.stdout.write('\n')
    else:
        sys.stdout.write(str(s)+'\n')


def main():
    np = neopixel.NeoPixel(machine.Pin(2), config.num_leds)
    ms_per_frame = 1000/config.fps
    last_frame = time.ticks_ms() - ms_per_frame
    while True:
        while last_frame + ms_per_frame > time.ticks_ms():
            pass
        last_frame = time.ticks_ms()
        color_a = random_color()
        color_b = random_color()
        say(color_a)
        say(color_b)
        say()
        for i in range(np.n):
            np[i] = pix_lerp(color_a,color_b,float(i)/np.n)
        np.write()


    # connect_to_wifi()
    # print('done connecting')
    # text = wget('https://raw.githubusercontent.com/mullinmax/esp32-programmer/master/main.py')

    # with open(output.txt,'w') as f:
        # f.write(text)


