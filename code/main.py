import neopixel
import sys
import time
import math

import config
from pixel import pixel
from color import color


def say(s=None):
    if s is None:
        sys.stdout.write('\n')
    else:
        sys.stdout.write(str(s)+'\n')

def black(pixels):
    for p in pixels:
        p.color = color(0,0,0)

def white_walk(pixels, t, n):
    for p in pixels:
        x = p.vector.x
        if (x+int(t)) % 3 == 0:
            p.color = color(255,255,255)

def cycle_through(values, seconds, t):
    return values[int(t/seconds)%len(values)]


def render(pixels, t):
    # black(pixels)
    cycle = cycle_through(range(len(pixels[0].locator_pattern)), 1/17.0, t)

    for p in pixels:
        p.color = p.locator_pattern[cycle]
        

def main():
    np = neopixel.NeoPixel(config.led_pin, config.num_leds)
    
    pixels = [pixel(color(0,0,0), v, i) for i,v in enumerate(config.led_vectors)]
    for p in pixels:
        p.set_locator_pattern(config.num_leds)

    ms_per_frame = 1000/config.fps
    next_frame = time.ticks_ms()
    while True:

        # render(pixels, next_frame/1000.0)
        
        cycle = cycle_through(range(len(pixels[0].locator_pattern)), ms_per_frame*2.0, next_frame)

        for i, p in enumerate(pixels):
            #ws2812 goes in g,r,b order
            np[i] = p.locator_pattern[cycle].get_grb()

        if next_frame > time.ticks_ms():
            ms_per_frame -= (next_frame - time.ticks_ms())/2
        else:
            ms_per_frame += 1
        say('fps:'+str(1000.0/ms_per_frame))

        # hold until it's time to render the next frame
        while next_frame > time.ticks_ms():
            pass
        
        np.write()
        next_frame = time.ticks_ms()+ms_per_frame # calculate when the next frame needs to be rendered
