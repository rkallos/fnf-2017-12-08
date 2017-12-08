import cv2
import numpy as np

img = cv2.imread('images/pills.png')

def kmeans(input, n_clusters):
    M = input.reshape((-1, 3))
    M = np.float32(M)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret, label, center = cv2.kmeans(M, n_clusters, None, criteria, 10,
                                    cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    output = center[label.flatten()]
    output = output.reshape((input.shape))
    return output

km2 = kmeans(img, 2)
km4 = kmeans(img, 4)
km8 = kmeans(img, 8)

out = np.vstack((np.hstack((img, km2)), np.hstack((km4, km8))))
cv2.imwrite('output/ex04.png', out)
