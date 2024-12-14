import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
def log_transform(image, c):
    img_array = np.array(image)
    transformed = c * np.log1p(img_array)
    transformed = (transformed / transformed.max()) * 255
    transformed = np.array(transformed, dtype=np.uint8)
    return Image.fromarray(transformed)

image_path = 'tire.jpg'
original_image = Image.open(image_path)
plt.figure(figsize=(12, 8))
plt.subplot(2, 3, 1)
plt.imshow(original_image)
plt.title('Original Image')
plt.axis('off')
for i, c in enumerate(range(1, 6), start=2):
    transformed_image = log_transform(original_image, c)
    plt.subplot(2, 3, i)
    plt.imshow(transformed_image)
    plt.title(f'Log Transform (c={c})')
    plt.axis('off')

plt.tight_layout()
plt.show()