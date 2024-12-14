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

# Create the sharpening kernel
kernel = np.array([[0, -3, 0], [-3, 15, -3], [0, -3, 0]])

# Sharpen the image
sharpened_image = cv2.filter2D(image, -10, kernel)

#Save the image
cv2.imwrite('sharpened_image.jpg', sharpened_image)

#Plot the sharpened image
plt.subplot(1, 2, 2)
plt.title("Sharpening")
plt.imshow(sharpened_image)
plt.show()