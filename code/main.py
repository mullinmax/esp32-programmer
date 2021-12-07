import time
import math

import config
from animation import animation

def locator(**kwargs):
    if kwargs['frame_num'] < 0:
        return (0, 0, 255)
    # sel = 1 << kwargs['frame_num']
    # if kwargs['vector'].x & sel:
    #     return (100,30,50)
    # else:
    #     return (0,0,0)   
    prev =locator(vector=kwargs['vector'], frame_num = kwargs['frame_num']-1)
    sel = 1 << kwargs['frame_num']
    if kwargs['vector'].x & sel:
        return (prev[2], prev[0], prev[1])
    else:
        return (prev[1], prev[2], prev[0])

def main():
    num_frames = math.ceil(math.log2(config.num_leds))
    a = animation(config.fps, num_frames, locator, config.led_vectors, config.led_pin)
    last_time = 0
    counter = 0
    while True:
        if a.display():
            counter += 1
        if counter >= 100:
            this_time = time.ticks_ms()
            print('fps:', 100*1000/(this_time - last_time))
            last_time = this_time
            counter = 0