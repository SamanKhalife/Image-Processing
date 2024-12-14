#Import the necessary libraries
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image
image = cv2.imread('sample.jpg')

#Plot the original image
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Equalize the histogram
equalized_image = cv2.equalizeHist(gray_image)

#Save the equalized image
cv2.imwrite('equalized.jpg', equalized_image)

#Plot the equalized image
plt.subplot(1, 2, 2)
plt.title("equalized")
plt.imshow(equalized_image)
plt.show()