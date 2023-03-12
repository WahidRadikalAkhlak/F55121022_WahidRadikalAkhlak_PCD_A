import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
img = cv2.imread('gambar4.jpg', 0)

# Calculate the histogram using cv2.calcHist()
hist, bins = np.histogram(img.ravel(), 256, [0, 256])

# Plot the histogram using matplotlib
plt.hist(img.ravel(), 256, [0, 256])
plt.title('Histogram')
plt.xlabel('Intensity')
plt.ylabel('Frequency')
plt.show()
