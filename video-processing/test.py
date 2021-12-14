import cv2
video = cv2.VideoCapture('tree.mp4')
success,image = video.read()

images = []
while success:
  success,image = video.read()
  images.append(image)

print(len(images))

# cv2.imshow('first frame',images[0])
# cv2.waitKey(0)

diffs = []
for i in range(1, len(images)-1):
    diffs.append(cv2.subtract(images[i-1], images[i]))

# cv2.imshow('first frame',diffs[0])
# cv2.waitKey(0)

means = []
for diff in diffs:
    means.append(cv2.mean(diff))

# print(means)

mean_of_means = [0,0,0]
for mean in means:
    mean_of_means[0] += mean[0]
    mean_of_means[1] += mean[1]
    mean_of_means[2] += mean[2]

mean_of_means[0] /= len(images)
mean_of_means[1] /= len(images)
mean_of_means[2] /= len(images)

print(mean_of_means)

above_mean = []
for mean in means:
    if mean[0] > mean_of_means[0] or mean[1] > mean_of_means[1] or mean[2] > mean_of_means[2]:
        above_mean.append(1)
    else:
        above_mean.append(0)

print(''.join([str(m) for m in above_mean]))

for diff, above in zip(diffs, above_mean):
    if above:
        for x in range(4):
            for y in range(4):
                diff[x][y] = (255,255,255)
    cv2.imshow('is above?',diff)
    cv2.waitKey(0)

