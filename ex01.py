import cv2
import numpy as np

img = cv2.imread('images/blur.png')

def avgfilter(input, kernelsize):
    # TODO: Create an averaging kernel
    # TODO: Apply the averaging kernel to input
    return output

avg3 = avgfilter(img, 3)
avg5 = avgfilter(img, 5)
avg10 = avgfilter(img, 10)

out = np.vstack((np.hstack((img, avg3)), np.hstack((avg5, avg10))))
cv2.imwrite('output/ex01.png', out)
