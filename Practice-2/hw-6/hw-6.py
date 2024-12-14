import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def gamma_correction(image, gamma):
    img_array = np.array(image) / 255.0
    corrected_array = np.clip(img_array ** gamma, 0, 1)
    corrected_image = (corrected_array * 255).astype(np.uint8)
    return Image.fromarray(corrected_image)

image_path = 'Picture.png'
original_image = Image.open(image_path)
gamma_value = 2.2
gamma_corrected_image = gamma_correction(original_image, gamma_value)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(original_image)
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(gamma_corrected_image)
plt.title(f'Gamma Corrected Image (Gamma={gamma_value})')
plt.axis('off')
plt.tight_layout()
plt.show()