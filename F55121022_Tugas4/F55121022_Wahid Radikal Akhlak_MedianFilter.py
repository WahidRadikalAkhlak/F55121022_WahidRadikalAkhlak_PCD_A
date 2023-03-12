import cv2

# Load image
img = cv2.imread('gambar3.jpeg')
img = cv2.resize(img, (321, 523))

# Define kernel size
ksize = 5

# Apply median filter
filtered_img = cv2.medianBlur(img, ksize)

# Display original and filtered image
cv2.imshow('Original Image', img)
cv2.imshow('Filtered Image', filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
