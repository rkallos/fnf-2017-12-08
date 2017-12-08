import cv2
import numpy as np

img = cv2.imread('images/penguin.png')

med3 = cv2.medianBlur(np.copy(img), 3)
med5 = cv2.medianBlur(np.copy(img), 5)
med10 = cv2.medianBlur(np.copy(img), 11)

out = np.vstack((np.hstack((img, med3)), np.hstack((med5, med10))))
cv2.imwrite('output/ex03.png', out)
