import cv2 as cv
import numpy as np

# shape of mask & img must be sme ⭐⭐

img = cv.imread('Resources\Photos\cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2],dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(img,img, mask=mask)
cv.imshow('masked',masked)

cv.waitKey(0)