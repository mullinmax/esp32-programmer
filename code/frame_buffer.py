from frame import frame
import time

class frame_buffer():
    def __init__(self, pin, led_vectors, max_size, render_function, fps):
        self.pin = pin
        self.led_vectors = led_vectors
        self.num_leds = len(self.led_vectors)
        
       
        self.ms_per_frame = 1000.0/fps
        
        self.max_size = max_size
        self.buffer = []
        self.used_frames = []
        
        self.render_function = render_function

        self.render_a_frame()

    def render_a_frame(self):
        if len(self.buffer) >= self.max_size:
            return

        f = None
        if len(self.used_frames) > 0:
            f = self.used_frames.pop() 
            f.is_rendered = None
        else:
            f = frame(0, self.pin, self.led_vectors, self.render_function)

        if len(self.buffer):
            f.target_time = self.buffer[-1].target_time + self.ms_per_frame
        else:            
            f.target_time = time.ticks_ms() + self.ms_per_frame

        f.render()
        self.buffer.append(f)

    def display_a_frame(self):
        f = self.buffer[0]
        if f.target_time < time.ticks_ms() and f.is_rendered:
            f.display()
            self.used_frames.append(self.buffer[0])
            self.buffer = self.buffer[1:]
            self.update_fps()
            return True
        return False 

    def update_fps(self):      
        pass
        # if len(self.buffer) >= self.max_size * 0.8:
        #     self.ms_per_frame = self.ms_per_frame * 0.9
        
        # if len(self.buffer) <= 2:
        #     self.ms_per_frame = self.ms_per_frame * 1.1
        
        