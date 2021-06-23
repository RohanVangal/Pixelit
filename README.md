# Pixircle (Pixelit Branch)
Pixelate an input picture (converted to greyscale) and substitute pixels with a circle of size corresponding with greyscale value.

### Files
- pixelit.py : Python 3.9 file
- srcimg.jpeg : source image
- output.jpg : output image file

### Process
The project was developed using python 3.9 using OpenCV, Numpy and PyCairo
The process includes:
1. Reading an input image
2. Converting the input image to grayscale
3. Resizing the image to pixellate it
4. Generating a matrix of values 0 (black) - 255 (white)
5. Plotting circles corresponding to each value on a Cairo canvas
6. Save the generated image

### Settings
1. IMG_PX_SCALE - percentage of resolution you want to scale down to
2. BLOCK_SIZE - square size to replace each pixel, in pixels 
3. SIZE_CORRECTION - reduction or increment on the maximum size of the circle
4. COLOUR_R,COLOUR_G,COLOUR_B - Colour settings of the circles value 0-1 (decimal)

### Possible Modifications
