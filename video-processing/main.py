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
        normalized[i] = round((el - minimum)/scale, 2)
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
# for i in range(len(video_phase_diffs)):
#     print(video_phase_diffs[i])

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


print(video_phase_diffs[best_error_video_phase])
# for img in video_phases[best_error_video_phase][best_error_led_phase:best_error_led_phase+num_led_frames]:
#     cv2.imshow('selected_frame',img)
#     cv2.waitKey(0)

video_seq = video_phases[best_error_video_phase][best_error_led_phase:best_error_led_phase+num_led_frames]

width = video_seq[0].shape[0]
height = video_seq[0].shape[1]
# all_pixels = sum([[(x,y) for y in range(height)] for x in range(width)], [])
# num_pixels = len(all_pixels)

def mean_comp(mean, raw, led):
    if (raw[0] < mean[0]) != (led[0] == 0):
        return False
    if (raw[1] < mean[1]) != (led[1] == 0):
        return False
    if (raw[2] < mean[2]) != (led[2] == 0):
        return False
    return True

    

# for each pixel
noise_ratio = 1.25
for x in range(100, 200):#range(0, width, 2):
    for y in range(100,200):#range(0, height, 2):
        # find mean value across all frames
        mean = [0,0,0]
        values = [f[x][y] for f in video_seq]
        mean[0] = sum([v[0] for v in values])/len(video_seq)
        mean[1] = sum([v[1] for v in values])/len(video_seq)
        mean[2] = sum([v[2] for v in values])/len(video_seq)

        for f in video_seq:
            f[x][y][0] = 0 if (f[x][y][0] < noise_ratio * mean[0]) else 255
            f[x][y][1] = 0 if (f[x][y][1] < noise_ratio * mean[1]) else 255
            f[x][y][2] = 0 if (f[x][y][2] < noise_ratio * mean[2]) else 255
    
        potential_matches = range(len(led_config.led_vectors))
        for i, f in enumerate(video_seq):
            potential_matches = [m for m in potential_matches if mean_comp(mean, f[x][y], a.frames[i][m])]
        
        if len(potential_matches) == 0:
            video_seq[0][x][y] = (0,0,0)
        else:
            print(x, y, potential_matches)
            video_seq[0][x][y] = (255,255,255)
    print(round(100.0*x/width, 2))
        
        

for img in video_seq:
    cv2.imshow('selected_frame',img)
    cv2.waitKey(0)

# for each pixel    
    # potential_matches
    # for each frame
        # filter potential_matches with same value as pixel
        # if potential_matches = 0 
            # break
    #pixel = potential_matches
            



# threshold = 30
# led_matches = []
# for led in range(len(led_config.led_vectors)):
#     pattern = [f[led] for f in a.frames]
#     potential_matches = all_pixels.copy()
#     for i in range(1, len(pattern)-1):
#         if pattern[i-1][0] < pattern[i][0]: #green       
#             potential_matches = [m for m in potential_matches if video_seq[i][m[0]][m[1]][1] > video_seq[i-1][m[0]][m[1]][1] + threshold]
#         if pattern[i-1][1] < pattern[i][1]: #red
#             potential_matches = [m for m in potential_matches if  video_seq[i][m[0]][m[1]][0] > video_seq[i-1][m[0]][m[1]][1] + threshold]
#         if pattern[i-1][2] < pattern[i][2]: #blue                           
#             potential_matches = [m for m in potential_matches if  video_seq[i][m[0]][m[1]][2] > video_seq[i-1][m[0]][m[1]][1] + threshold]
#     led_matches.append(potential_matches)
#     print(led, [sum(x)/len(x) for x in zip(*potential_matches)], len(potential_matches))

# match_img = video_seq[0].copy()

# for matches in led_matches:
#     for match in matches:
#         match_img[match[0]][match[1]] = (0,0,255)


# cv2.imshow('selected_frame',match_img)
# cv2.waitKey(0)

# find pixels that match animation pixels (regions/bluring?)

# find center of mass of pixels that match each led

# output x-y coordinates for each pixel
