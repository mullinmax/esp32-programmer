import cv2

import config

from led_driver.main import locator, locator_pattern
from led_driver.animation import animation
from led_driver import config as led_config

# recreate animation
num_led_frames = len(locator_pattern(0))
a = animation(led_config.fps, num_led_frames, locator, led_config.led_vectors, led_config.led_pin)
# for f in a.frames:
#     print(f)

#Calculate constants
video_frames_per_led_frame = int(config.fps / led_config.fps)
video_cycle_frames = int(num_led_frames * video_frames_per_led_frame)

# calculate expected frame-shift pattern
shift_amt = []
for cur_f, prev_f in zip(a.frames, [a.frames[-1]]+a.frames[:-1]):
    shift_amt.append(0)
    for cur_p, prev_p in zip(cur_f, prev_f):
        if cur_p != prev_p:
            shift_amt[-1] += 1
    # print(cur_f, prev_f, shift_amt[-1])
# print(shift_amt)

# normalize shift pattern
def normalize_list(l):
    normalized = [0 for i in range(len(l))]
    minimum = min(l)
    scale = max(l) - minimum
    for i, el in enumerate(l):
        normalized[i] = round(10*(el - minimum)/scale)
    return normalized
shift_amt = normalize_list(shift_amt)
# print(shift_amt)

# open video
video = cv2.VideoCapture('tree.mp4')
success,image = video.read()
 
# read video into images
images = []
while success:
  success,image = video.read()
  images.append(image)

# create video phases
video_phases = []
for offset in range(video_frames_per_led_frame):
    phase = []
    for i in range(offset, len(images), video_frames_per_led_frame):
        phase.append(images[i])
    video_phases.append(phase)

# calculate image diffs for each phase
video_phase_diffs = []
for p in video_phases:
    video_phase_diff = []
    for i in range(1, len(p)-1):
        mean_color = cv2.mean(cv2.subtract(p[i-1], p[i]))
        video_phase_diff.append(sum(mean_color))
    video_phase_diffs.append(normalize_list(video_phase_diff))
for i in range(len(video_phase_diffs)):
    print(video_phase_diffs[i])

# find phase offset of shifts to pattern
best_error = 1000 * num_led_frames
best_error_led_phase = 0
best_error_video_phase = 0
for led_phase in range(num_led_frames):
    led_sequence = shift_amt[-led_phase:]+shift_amt[:-led_phase]
    for v in range(len(video_phase_diffs)):
        error = 0
        for i, diff in enumerate(video_phase_diffs[v]):
            error += abs(diff - led_sequence[i%len(led_sequence)])
        if error < best_error:
            best_error = error
            best_error_led_phase = led_phase
            best_error_video_phase = v
print(best_error)
print(best_error_led_phase)
print(best_error_video_phase)
    


# get sample frames from median of each shift

# find pixels that match animation pixels (regions/bluring?)

# find center of mass of pixels that match each led

# output x-y coordinates for each pixel
