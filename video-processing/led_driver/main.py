import math
import random
import config
import animation


white = (255,255,255)
cream = (255,255,60)
black = (0,0,0)
red = (0,255,0)
orange = (125,255,0)
yellow = (255,255,255)
green = (255,0,0)
blue = (0,0,255)
purple = (0,166,255)
cyan = (255,0,255)

color_wheel = [cream, red, orange, yellow, green, blue, purple]

def parity_bit(n):
    i = 1
    p = 0
    while i <= n:
        if i & n:
            p += 1
        i = i << 1
    return p % 2

# def locator_pattern(i):
#     pattern = [black, black, black] # start sequence 
#     pattern += [red if bool(i >> shift & 1) else green for shift in range(8)]
#     if parity_bit(i):
#         pattern.append(blue)
#     else:
#         pattern.append(black)
#     return pattern

# def locator(**kwargs):
#     pattern = locator_pattern(kwargs['vector'].x)
#     return pattern[kwargs['frame_num']]  

def lfsr(i, num_bits):
    reg = i
    bits = 0
    for b in range(num_bits):
        next_bit = reg ^ (reg >> 1) ^ (reg >> 2) ^ (reg >> 7)
        reg = (reg >> 1) | (next_bit << 127)
        bits = bits << 1 | next_bit
    pattern = []
    print(bin(bits))
    for b in range(num_bits):
        if (bits >> b) & 1:
            pattern.append(cream)
        else:
            pattern.append(black)
    return pattern

def lerp(a, b, r):
    return r*(b-a)+a

def color_lerp(a, b, r):
    return [int(lerp(a[0], b[0], r)), int(lerp(a[1], b[1], r)), int(lerp(a[2], b[2], r))]

def smooth(frames, ratio):
    for f in range(0, len(frames), ratio):
        for fr in range(ratio):
            for i in range(len(frames[0])):
                frames[f-ratio+fr][i] = color_lerp(frames[f-ratio][i], frames[f][i], fr/ratio)

            

def pst_twinkle(**kwargs):
    print('getting pallet')
    pallet = get_pst_pallet()
    print('rendering')
    for time, _ in enumerate(kwargs['times']):
        for led, _ in enumerate(kwargs['vectors']):
            kwargs['frames'][time][led] = random.choice(pallet)
    print('smoothing')
    smooth(kwargs['frames'], config.twinkle_smooth_ratio)            
    return

def get_pst_pallet():
    primary = random.choice(color_wheel)
    secondary = random.choice(color_wheel)
    tertiary = random.choice(color_wheel)
    while secondary == primary:
        secondary = random.choice(color_wheel)
    while secondary == tertiary or tertiary == primary:
        tertiary = random.choice(color_wheel)
    return [primary]*6+[secondary]*3+[tertiary]*1



def main():
    a = animation.animation(config.fps, config.num_frames, pst_twinkle, config.led_vectors, config.led_pin)
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