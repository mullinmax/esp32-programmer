# https://github.com/micropython/micropython/blob/841eeb158e1d43ba34e4ee629143e10a2c4505ff/drivers/neopixel/neopixel.py

import neopixel

class frame():
    def __init__(self, target_time, pin, led_vectors, render_function):
        self.target_time = target_time
        self.led_vectors = led_vectors
        self.np = neopixel.NeoPixel(pin, len(led_vectors))
        self.is_rendered = None
        self.render_function = render_function

    def time(self, time=None):
        if time:
            self.target_time = time
            self.is_rendered = None
        return time

    def render(self):
        if self.is_rendered:
            return
        self.is_rendered = False # we need to do this since it could be None
        
        # run asynchronously
        self.render_function(self.np, self.led_vectors, self.target_time) 
        self.is_rendered = True

    def display(self):
        # run asynchronously
        self.np.write()
