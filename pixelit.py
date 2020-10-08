# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:37:51 2020

@author: RoSaVa
"""
import numpy as np
import cv2

# Source image paths
IMG_PATH = 'srcimg.jpg'
PIX_PATH = 'pix.jpg'

# Degree of pixelation: Image is scaled down to the following percentage
IMG_PX_SCALE = 2

# Contrast value- the lower the value the brighter the image
CONTRAST_THRESHOLD = 50

# Read pixel source and convert to grayscale
pix = cv2.imread(PIX_PATH,cv2.IMREAD_GRAYSCALE)
pix = pix.astype('int')
# 'White' pixel
pix_zeros = np.ones(pix.shape, dtype=int)*255
# Read original image in grayscale
img = cv2.imread(IMG_PATH,cv2.IMREAD_GRAYSCALE)
imgpx_scale = IMG_PX_SCALE/100
img_h, img_w = img.shape

# Resize image
px_size =  ((int)(img_w*imgpx_scale)),((int)(img_h*imgpx_scale))
imgpx_resize = cv2.resize(img, px_size, interpolation=cv2.INTER_LINEAR)

# Convert image into a binary map based on threshold (contrast value)
(thresh, imgpx_bin) = cv2.threshold(imgpx_resize, CONTRAST_THRESHOLD, 1, cv2.THRESH_BINARY)

# Filling a matrix with input pixels based on binary map
w,h = px_size
final_img = []

for i in range (h):
    temp = [None] * w
    for j in range (w):
        if imgpx_bin[i][j] == 0:
            temp [j] = pix
        else:
            temp [j] = pix_zeros
    # concatenate along vertical axis        
    temp2 = np.concatenate(temp,axis = 1)
    if i == 0:
        final_img = temp2
    else:
        # concatenate along horizontal axis 
        final_img = np.concatenate((final_img,temp2))

cv2.imwrite('output.jpg', final_img)
