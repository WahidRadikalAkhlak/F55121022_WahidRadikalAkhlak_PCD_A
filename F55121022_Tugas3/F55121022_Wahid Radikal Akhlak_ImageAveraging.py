import cv2
import numpy as np

# Load the images
img1 = cv2.imread('gambar1.jpeg')
img2 = cv2.imread('gambar2.jpeg')
img2 = cv2.resize(img2, (595, 409))

# Average the images
avg_img = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

# Display the averaged image
cv2.imshow('Averaged Image', avg_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
