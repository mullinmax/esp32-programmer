import time
import math

import config
from frame_buffer import frame_buffer

def cycle_through(values, seconds, t):
    return values[int(t/seconds)%len(values)]

def locator(vector, time_ms):   
    num_bits = 7#math.ceil(math.log2(config.num_leds))
    cycle = cycle_through(range(num_bits), 0.5, time_ms/1000.0)
    if bool((vector.x >> cycle) & 1):
        return (100,30,50)
    else:
        return (0,0,0)   

def main():
    fb = frame_buffer(config.led_pin, config.led_vectors, config.frame_buffer_size, locator, config.fps)
    while True:
        fb.render_a_frame()
        fb.display_a_frame()
        print(len(fb.buffer), fb.ms_per_frame, fb.buffer[0].target_time - time.ticks_ms())
    