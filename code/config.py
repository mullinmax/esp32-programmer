from machine import Pin

from vector import vector

wifi = {
    'ssid': 'This LAN is My LAN',
    'password':'allhailhypnotoad'
}

fps = 60
led_scale = 255
num_leds = 400
led_pin = Pin(2)
led_vectors = [vector(i,i,i) for i in range(num_leds)]


