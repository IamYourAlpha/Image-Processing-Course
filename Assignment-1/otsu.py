import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('./1.png',0)


# Otsu's thresholding after Gaussian filtering
blur = cv.GaussianBlur(img,(5,5),0)
ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)


plt.imshow(th3,'gray')
plt.show()
