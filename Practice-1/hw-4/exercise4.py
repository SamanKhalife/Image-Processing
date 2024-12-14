#  برنامه ای بنویسید که عکس  pappers.png را بخواند و هر چنل ان را نمایش دهد
# (نوع ۱  نوع ۲  نوع ۳ )

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def display_channels(image, title):
    channels = ['Red', 'Green', 'Blue']
    types = ['Type 1 (Binary)', 'Type 2 (8-bit)', 'Type 3 (Original)']

    fig, axs = plt.subplots(3, 3, figsize=(15, 15))
    fig.suptitle(title, fontsize=16)

    for i, channel in enumerate(channels):
        # Extract channel
        channel_array = np.array(image.getchannel(i))

        # Type 1: Binary
        type1 = Image.fromarray((channel_array > 128).astype(np.uint8) * 255)

        # Type 2: 8-bit (already in this format)
        type2 = Image.fromarray(channel_array)

        # Type 3: Original (same as Type 2 for individual channels)
        type3 = type2

        for j, (img, type_name) in enumerate(zip([type1, type2, type3], types)):
            axs[i, j].imshow(img, cmap='gray')
            axs[i, j].set_title(f'{channel} - {type_name}')
            axs[i, j].axis('off')

    plt.tight_layout()
    plt.show()

image = Image.open('pappers.png')

display_channels(image, 'Channels of pappers.png')

print(f"Image dimensions: {image.size}")
print(f"Image format: {image.format}")
print(f"Image mode: {image.mode}")