class color():

    def __init__(self, r, g, b, max_value=255):
        self.r = r
        self.g = g
        self.b = b
        self.max_value = float(max_value)

    def get_rgb(self):
        return (self.r, self.g, self.b)

    def get_grb(self):
        return (self.g, self.r, self.b)

    def get_hsv(self):
        # change the range from 0..255 to 0..1:
        r = self.r / self.max_value
        g = self.g / self.max_value
        b = self.b / self.max_value

        cmax = max(r, g, b)
        cmin = min(r, g, b)
        diff = cmax-cmin
    
        # hue
        if cmax == cmin:
            h = 0
        elif cmax == r:
            h = (60 * ((g - b) / diff) + 360) % 360
        elif cmax == g:
            h = (60 * ((b - r) / diff) + 120) % 360
        elif cmax == b:
            h = (60 * ((r - g) / diff) + 240) % 360
    
        # saturation
        if cmax == 0:
            s = 0
        else:
            s = (diff / cmax) * 100
    
        # value / brightness
        v = cmax * 100
        return h, s, v

    def set_hsv(self, h, s, v):
        c = v*s
        x = c*(1-math.abs((h/60)%2-1))
        m=c-c
        
        formulas = [
            (c,x,0),
            (x,c,0),
            (0,c,x),
            (0,x,c),
            (x,0,c),
            (c,0,x),
        ]

        R,G,B = formulas[int(h/60)]
        self.r = R + m
        self.g = G + m
        self.b = B + m

    def h(self, h=None):
        hsv = self.get_hsv()
        if h is not None:
            hsv[0] = h
            self.set_hsv(hsv)
        return hsv[0]

    def s(self, s=None):
        hsv = self.get_hsv()
        if s is not None:
            hsv[1] = s
            self.set_hsv(hsv)
        return hsv[1]

    def v(self, v=None):
        hsv = self.get_hsv()
        if v is not None:
            hsv[2] = v
            self.set_hsv(hsv)
        return hsv[2]

    def __str__(self):
        return '('+str(self.r)+','+str(self.g)+','+str(self.b)+')'