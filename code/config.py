import machine

from vector import vector

machine.freq(240000000) #clock to highest speed

wifi = {
    'ssid': 'This LAN is My LAN',
    'password':'allhailhypnotoad'
}

fps = 30
frame_buffer_size = 10
led_scale = 255
num_leds = 300
led_pin = machine.Pin(2)
led_vectors = [vector(i,i,i) for i in range(num_leds)]