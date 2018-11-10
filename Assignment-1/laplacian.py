import cv2
import numpy as np
from matplotlib import pyplot as plt

img0 = cv2.imread('./1.png',)

# converting to gray scale
gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

# remove noise
img = cv2.GaussianBlur(img0,(3,3),0)

# convolute with proper kernels
laplacian = cv2.Laplacian(img)
laplacian = np.invert(laplacian)
plt.imshow(laplacian,cmap = 'gray')

plt.show()


