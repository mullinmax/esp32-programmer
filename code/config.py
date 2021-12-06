from machine import Pin

from vector import vector

wifi = {
    'ssid': 'This LAN is My LAN',
    'password':'allhailhypnotoad'
}

fps = 30
frame_buffer_size = 10
led_scale = 255
num_leds = 50
led_pin = Pin(2)
led_vectors = [vector(i,i,i) for i in range(num_leds)]


