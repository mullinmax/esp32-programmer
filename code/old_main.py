import time
import math

import config
from frame_buffer import frame_buffer

def cycle_through(values, seconds, t):
    return values[int(t/seconds)%len(values)]

@micropython.native
def locator(np, led_vectors, time_ms):   
    num_bits = math.ceil(math.log2(config.num_leds))
    cycle = cycle_through(range(num_bits), 0.2, time_ms/1000.0)
    sel = 1 << cycle
    white = [255,255,255]
    black = [0,0,0]
    
    np.buf = bytearray(sum([white if i & sel else black for i in range(len(led_vectors))], []))
     
    # for i in range(len(led_vectors)):
        # np[i] = (100,30,50)
    # num_bits = 7#math.ceil(math.log2(config.num_leds))
    # cycle = cycle_through(range(num_bits), 0.5, time_ms/1000.0)
    # if bool((vector.x >> cycle) & 1):
    #     return (100,30,50)
    # else:
    #     return (0,0,0)   

def main():
    fb = frame_buffer(config.led_pin, config.led_vectors, config.frame_buffer_size, locator, config.fps)
    while True:
        t0 = time.ticks_ms()
        fb.render_a_frame()
        t1 = time.ticks_ms()
        fb.display_a_frame()
        t2 = time.ticks_ms()
        print('render time:',t1-t0,'display time:', t2-t1)
        # print(len(fb.buffer), fb.ms_per_frame, fb.buffer[0].target_time - time.ticks_ms())
    