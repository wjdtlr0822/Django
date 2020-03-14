############################################################# 연습1##
# import cv2
# import matplotlib.pyplot as plt
#
# img=cv2.imread('test.jpg',cv2.IMREAD_COLOR)
# plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
# plt.show()
# print(img.shape)
# print(img.size)
#
# img2=cv2.imread('test.jpg',cv2.IMREAD_GRAYSCALE)
# plt.imshow(cv2.cvtColor(img2,cv2.COLOR_GRAY2RGB))
# plt.show()
# print(img2.shape)
# print(img2.size)
#
# cv2.waitKey(0)
################################################ 연습 2

import cv2

img1=cv2.imread('test.jpg')
img=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret,img_bi=cv2.threshold(img,190,255,cv2.THRESH_BINARY) #바이너리로 변경
cv2.imshow('re',img_bi)
cv2.waitKey(0)
img_bi1=cv2.bitwise_not(img_bi) # 검흰 반전

contours,hi=cv2.findContours(img_bi1,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img1,contours,-1,(255,0,255),2)

cv2.imshow('re',img1)
cv2.waitKey(0)