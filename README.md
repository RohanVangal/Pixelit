# Pixelit
Pixelate a picture with a custom pixel.

### Files
- pixelit.py : Python 3.7 file
- srcimg.jpeg : source image
- pix.jpg : source pixel image (square)
- output.jpg : output image file

### Process
The project was developed using python 3.7 using OpenCV and Numpy. 
The process includes:
1. Reading an input image
2. Converting the input image to grayscale
3. Resizing the image to pixellate it
4. Generating a matrix of 0s and 1s decided by a threshold grey value
5. Reading input pixel and generating a corresponding blank pixel
6. Creating a new matrix using the binary matrix of the original image as a template to place the input pixel and the blank pixels
7. Output the image

### Possible Modifications
- Instead of a binary matrix, generate a range of values based on threshold ranges. Then, substitute the values with different input pixels.
- Improve program execution. There should be an easier way to map the pixels onto the matrix without the loops.
