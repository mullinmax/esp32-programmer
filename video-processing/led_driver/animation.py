try:
    import neopixel
except:
    print('neopixel not available, must not be micropython')

import time

class animation():
    def __init__(self, fps, num_frames, render_function, led_vectors, pin):       
        self.num_frames = num_frames
        self.render_function = render_function
        self.led_vectors = led_vectors
        self.pin = pin

        try:
            self.frames = [neopixel.NeoPixel(pin, len(led_vectors)) for f in range(num_frames)]
        except:
            self.frames = [[[0,0,0] for i in range(len(led_vectors))] for f in range(num_frames)]

        self.ms_per_frame = int(1000/fps)
        self.last_frame = -1
        self.timer = None

        self.render()

    def render(self):
        # func = self.render_function
        frame_times = [i*self.ms_per_frame for i in range(self.num_frames)]
        print('calling render function')
        self.render_function(vectors=self.led_vectors, times=frame_times, frames=self.frames)
        # print('patterns to frames')
        # for i, f in enumerate(self.frames):
        #     for led in range(len(self.led_vectors)):
        #         self.frames[i][led] = f[led]
        print('done rendering')
            

    def display(self):
        target_frame = int(time.ticks_ms()/self.ms_per_frame) % self.num_frames
        if self.last_frame != target_frame:   
            self.frames[target_frame].write()
            self.last_frame = target_frame
            return True
        return False

