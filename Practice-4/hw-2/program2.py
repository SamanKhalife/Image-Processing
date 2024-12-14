import numpy as np
from PIL import Image
image = Image.open('rice.png')
image_array = np.array(image)
if image_array.ndim == 3:
    image_array = np.mean(image_array, axis=2)

mean = np.mean(image_array)
variance = np.var(image_array)
std_deviation = np.std(image_array)
print(f"miangin: {mean}")
print(f"variance: {variance}")
print(f"enheraf: {std_deviation}")