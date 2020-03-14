# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.figure(figsize=(6,6))
# plt.subplot(1,2,1)
# plt.subplot(1,2,2)
# plt.show()

import cv2

img_gray=cv2.imread('고양이9.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('test',img_gray)
cv2.waitKey(0)