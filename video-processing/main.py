import config

from led_driver.main import locator, locator_pattern
from led_driver.animation import animation
from led_driver import config

def main():
    # recreate animation
    num_frames = len(locator_pattern(0))
    a = animation(config.fps, num_frames, locator, config.led_vectors, config.led_pin)

    # calculate expected frame-shift pattern
    
    # find phase offset of shifts to pattern

    # get sample frames from median of each shift

    # find pixels that match animation pixels (regions/bluring?)

    # find center of mass of pixels that match each led
    
    # output x-y coordinates for each pixel
    