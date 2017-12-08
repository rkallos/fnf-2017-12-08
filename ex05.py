import cv2
import numpy as np

img = cv2.imread('images/pills.png')

inp = cv2.cvtColor(np.copy(img), cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(inp, cv2.HOUGH_GRADIENT, 1, 20,
                           param1 = 50, param2 = 15,
                           minRadius = 10, maxRadius = 15)

out = np.copy(img)
circles = np.uint16(np.around(circles))
print(circles[0, :])
for i in circles[0, :]:
    cv2.circle(out, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cv2.circle(out, (i[0], i[1]), 2, (0, 0, 0), 3)

cv2.imwrite('output/ex05.png', np.hstack((img, out)))
