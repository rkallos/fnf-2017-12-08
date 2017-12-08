import cv2
import numpy as np

img = cv2.imread('images/moon.png')

def laplacian(input):
    kernel = np.array([]) # TODO: Add the Laplacian matrix
    lpc = cv2.filter2D(np.copy(input), -1, kernel)
    output = lpc # TODO: Fix negative values in lpc
    return output

def sharpen(input, lpcoef):
    lpc_img = laplacian(input)
    output = np.copy(input) + (lpc_img * lpcoef)
    return output

sharp50 = sharpen(img, 0.5)
sharp150 = sharpen(img, 1.5)
sharp200 = sharpen(img, 2.0)

out = np.vstack((np.hstack((img, sharp50)), np.hstack((sharp150, sharp200))))
cv2.imwrite('output/ex02.png', out)
