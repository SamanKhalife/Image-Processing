import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def threshold_image(image):
    img_array = np.array(image.convert('L'))
    mean_value = np.mean(img_array)
    thresholded = np.where(img_array > mean_value, 255, 0)
    return Image.fromarray(thresholded.astype(np.uint8)), mean_value

image_path = 'Picture.png'
original_image = Image.open(image_path)
thresholded_image, mean_value = threshold_image(original_image)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(original_image)
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(thresholded_image, cmap='gray')
plt.title(f'Thresholded Image (Mean={mean_value:.2f})')
plt.axis('off')
plt.tight_layout()
plt.show()