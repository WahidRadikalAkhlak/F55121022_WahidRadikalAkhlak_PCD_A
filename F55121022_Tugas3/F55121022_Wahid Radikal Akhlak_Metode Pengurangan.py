import cv2
import numpy as np

# Load the images
img1 = cv2.imread('gambar1.jpeg')
img2 = cv2.imread('gambar2.jpeg')
img2 = cv2.resize(img2, (595, 409))

# Convert the images to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Subtract the grayscale images
diff = cv2.subtract(gray1, gray2)

# Display the original images and the difference image side by side
cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)
cv2.imshow('Difference', diff)
cv2.waitKey(0)
cv2.destroyAllWindows()
