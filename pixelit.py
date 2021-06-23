"""
@Brief:         Accepts input image, converts it to greyscale and pixelaltes it.
                A new image is then generated placing circles of a size proportional to each pixel
@created:       23/06/2021
@author:        RoSaVa
@note:          Source image: https://www.gmcsubscriptions.com/product/black-white-issue-231-aug-19/
"""
import numpy as np
import cv2
import cairo
import math

# Source image paths
IMG_PATH = 'srcimg.jpg'
# Degree of pixelation: Image is scaled down to the following percentage
IMG_PX_SCALE = 10

# Read original image in grayscale
img = cv2.imread(IMG_PATH,cv2.IMREAD_GRAYSCALE)
imgpx_scale = IMG_PX_SCALE/100
img_h, img_w = img.shape

# Pixelated image size
px_size =  ((int)(img_w*imgpx_scale)),((int)(img_h*imgpx_scale))
w,h = px_size
#Resize image
imgpx_resize = cv2.resize(img, px_size, interpolation=cv2.INTER_LINEAR)

# #Size of square that replaces each pixel, in pixels
BLOCK_SIZE = 50
SIZE_CORRECTION = -3

# Colour settings of the circles value 0-1 (decimal)
COLOUR_R = 1
COLOUR_G = 1
COLOUR_B = 1

#Setting up Cairo surface to draw on
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, w*BLOCK_SIZE, h*BLOCK_SIZE)
ctx = cairo.Context(surface)

# ctx.set_source_rgb(1, 1, 1)             # white background
ctx.set_source_rgba(0.0, 0.0, 0.0, 0.0) # transparent black background
ctx.rectangle(0, 0, w*BLOCK_SIZE, h*BLOCK_SIZE)
ctx.fill()

for i in range (h):
    y = (int)((i+0.5)*BLOCK_SIZE)
    for j in range (w):
        x = (int)((j+0.5)*BLOCK_SIZE)

        #Setting Diameter
        dia = (imgpx_resize[i][j]/255)*(BLOCK_SIZE + SIZE_CORRECTION)
        #Drawing circle
        ctx.arc(x, y, dia, 0, 2*math.pi)
        ctx.set_source_rgb(COLOUR_R, COLOUR_G, COLOUR_B)
        ctx.fill()  

#Save Cairo surface as png
surface.write_to_png('output.jpg')
