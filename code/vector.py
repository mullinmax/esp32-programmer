class vector():

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, o):
        try:
            k = float(o)
            return vector(self.x * k, self.y * k, self.z * k)
        except ValueError:
            if isinstance(o, vector):
                return vector(self.x * o.x, self.y * o.y, self.z * o.z)
    
    def __add__(self, o):
        try:
            k = float(o)
            return vector(self.x + k, self.y + k, self.z + k)
        except ValueError:
            if isinstance(o, vector):
                return vector(self.x + o.x, self.y + o.y, self.z + o.z)
    
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+','+str(self.z)+')'