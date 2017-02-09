 
import cv2
import os
import numpy as np

# Load images
def image_make(file_name):
	folder='uploads'

	img1 = cv2.imread(os.path.join(folder,file_name))
	img2 = cv2.imread('last.png')

	#img1= cv2.resize(img1,(480,380),fx=0, fy=0, interpolation = cv2.INTER_NEAREST)


	r = 980.0 / img1.shape[1]
	dim = (980, int(img1.shape[0] * r))
	 
	# perform the actual resizing of the image and show it
	img1= cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)


	rows1,cols1,channels1 = img1.shape
	rows,cols,channels = img2.shape


	x= rows1-rows
	print rows1
	print img1.shape
	print img2.shape
	roi = img1[x:rows1, 0:cols ]

	img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
	ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
	mask_inv = cv2.bitwise_not(mask)

	img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
	img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

	dst = cv2.add(img1_bg,img2_fg)
	img1[x:rows1, 0:cols ] = dst

	#cv2.imshow('res',img1)
	cv2.imwrite(os.path.join(folder,file_name),img1)
#	cv2.waitKey(0)
#	cv2.destroyAllWindows()