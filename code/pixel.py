import math
from vector import vector
from color import color


class pixel():
    def __init__(self, color, vector, i):
        self.color = color
        self.vector = vector
        self.i = i 
        self.locator_pattern = None
        
    def set_locator_pattern(self, num_leds):
        num_bits = math.ceil(math.log2(num_leds))
        self.locator_pattern = [bool((self.i>>j) & 1) for j in range(num_bits)]
        self.locator_pattern.reverse()
        self.locator_pattern += [None]

        for k,v in enumerate(self.locator_pattern):
            if v is None:
                self.locator_pattern[k] = color(100,0,0)
            elif v:
                self.locator_pattern[k] = color(100,100,100)
            else:
                self.locator_pattern[k] = color(0,0,0)

    def __str__(self):
        return "'color':"+str(self.color)+",'vector':"+str(self.vector)+"}"