import neopixel
import time

class animation():
    def __init__(self, fps, num_frames, render_function, led_vectors, pin):       
        self.num_frames = num_frames
        self.render_function = render_function
        self.led_vectors = led_vectors
        self.pin = pin

        self.frames = [neopixel.NeoPixel(pin, len(led_vectors)) for f in range(num_frames)]
        self.ms_per_frame = int(1000/fps)
        self.last_frame = -1
        self.timer = None

        self.render()

    def render(self):
        func = self.render_function
        for frame_num, frame in enumerate(self.frames):
            target_time = frame_num * self.ms_per_frame
            for i, v in enumerate(self.led_vectors):
                frame[i] = func(vector=v, timer_ms = target_time, frame_num=frame_num)

    def display(self):
        target_frame = int(time.ticks_ms()/self.ms_per_frame) % self.num_frames
        if self.last_frame != target_frame:   
            self.frames[target_frame].write()
            self.last_frame = target_frame
            return True
        return False
