try:
    import machine
except:
    print('neopixel not available, must not be micropython')

import vector

try: # handle the non-micropython case
    led_pin = machine.Pin(2)
    machine.freq(240000000) #clock to highest speed
except:
    led_pin = 2

wifi = {
    'ssid': 'This LAN is My LAN',
    'password':'allhailhypnotoad'
}

fps = 30
led_scale = 255
num_leds = 50
led_vectors = [vector.vector(i,i,i) for i in range(num_leds)]

num_frames = 600

twinkle_smooth_ratio = 30
