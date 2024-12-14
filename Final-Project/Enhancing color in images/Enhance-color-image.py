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

# Convert the image from BGR to HSV color space
image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

# Adjust the hue, saturation, and value of the image
# Adjusts the hue by multiplying it by 1.2
image[:, :, 0] = image[:, :, 0] * 1.2
# Adjusts the saturation by multiplying it by 1.2
image[:, :, 1] = image[:, :, 1] * 1.2
# Adjusts the value by multiplying it by 1.2
image[:, :, 2] = image[:, :, 2] * 1.2

# Convert the image back to BGR color space
image2 = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)

#Save the image
cv2.imwrite('enhanced coloured.jpg', image2)

#Plot the enhanced image
plt.subplot(1, 2, 2)
plt.title("enhanced coloured")
plt.imshow(image2)
plt.show()