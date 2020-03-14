# import cv2 as cv
#
# img=cv.imread('test.jpg')
# img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# ret,img_bi=cv.threshold(img_gray,200,255,cv.THRESH_BINARY)
# img_bi1=cv.bitwise_not(img_bi)
# count,hi=cv.findContours(img_bi1,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
# img_re=cv.drawContours(img,count,-1,(0,0,255),3)
#
# print(count)
#
# cv.imshow('test',img)
# cv.waitKey(0)

import cv2
import pytesseract

img=cv2.imread('cap/cap1.PNG',cv2.IMREAD_COLOR)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresh,img_bi=cv2.threshold(img_gray,150,255,cv2.THRESH_BINARY)
# cv2.imshow('test',img_bi)
# cv2.waitKey(0)
text=pytesseract.image_to_string(img_bi,lang='eng',config='--psm 8 --oem 3')
print(text)
img_bi1=cv2.bitwise_not(img_bi)
contour,hi=cv2.findContours(img_bi1,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
img_draw=cv2.drawContours(img,contour,-1,(0,0,255),1)
#
# cv2.imshow('test',img)
# cv2.waitKey(0)