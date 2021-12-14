import config

from led_driver.main import locator, locator_pattern
from led_driver.animation import animation
from led_driver import config

def main():
    # recreate animation
    num_frames = len(locator_pattern(0))
    a = animation(config.fps, num_frames, locator, config.led_vectors, config.led_pin)

    # calculate expected frames per shift
    # get sample frames
    # render animation
    # find pixels that match animation pixels
    # find center of pixels for each led
    # output x-y coordinates for each pixel
    