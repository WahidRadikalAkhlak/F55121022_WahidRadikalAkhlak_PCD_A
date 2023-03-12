import cv2
import numpy as np

# Load image
img = cv2.imread('gambar1.jpeg')
img = cv2.resize(img, (362, 522))
# Define kernel size
ksize = 3

# Define kernel for max filter
kernel = np.ones((ksize,ksize),np.uint8)

# Apply max filter
filtered_img = cv2.dilate(img,kernel)

# Display original and filtered image
cv2.imshow('Original Image', img)
cv2.imshow('Filtered Image', filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
