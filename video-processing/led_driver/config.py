try:
    import machine
except:
    print('neopixel not available, must not be micropython')

from .vector import vector

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
frame_buffer_size = 10
led_scale = 255
num_leds = 300
led_vectors = [vector(i,i,i) for i in range(num_leds)]