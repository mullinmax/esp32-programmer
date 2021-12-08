import time
import math

white = (255,255,255)
black = (0,0,0)
red = (0,255,0)
green = (255,0,0)
blue = (0,0,255)

def parity_bit(n):
    i = 1
    p = 0
    while i <= n:
        if i & n:
            p += 1
        i = i << 1
    return p % 2

def locator_pattern(i):
    pattern = [black, white, black] # start sequence look for largest jump and fall in brightness for timing
    pattern += [red if bool(i >> shift & 1) else green for shift in range(8)]
    if parity_bit(i):
        pattern.append(blue)
    else:
        pattern.append(black)
    return pattern

def locator(**kwargs):
    pattern = locator_pattern(kwargs['vector'].x)
    return pattern[kwargs['frame_num']]  

def main():
    # importing here allows us to import in normal python
    from animation import animation
    import config
    num_frames = len(locator_pattern(0))
    a = animation(config.fps, num_frames, locator, config.led_vectors, config.led_pin)
    last_time = 0
    counter = 0
    while True:
        a.display()
        # if a.display():
        #     counter += 1
        # if counter >= 100:
        #     this_time = time.ticks_ms()
        #     print('fps:', 100*1000/(this_time - last_time))
        #     last_time = this_time
        #     counter = 0