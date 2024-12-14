# برنامه ای بنویسید که عکس  زیر را بگیرد و رزولوشن
# شدت روشنایی آنرا از 256 سطح (8 بیتی)  به  16 سطح (4 بیتی) کاهش دهد

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def reduce_brightness_resolution(image_path):
    image = Image.open(image_path).convert('L')

    img_array = np.array(image)

    img_4bit = (img_array // 16).astype(np.uint8)

    img_4bit_scaled = img_4bit * 16

    image_8bit = Image.fromarray(img_array)
    image_4bit = Image.fromarray(img_4bit_scaled)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    ax1.imshow(image_8bit, cmap='gray')
    ax1.set_title('تصویر اصلی (8 بیتی)')
    ax1.axis('off')

    ax2.imshow(image_4bit, cmap='gray')
    ax2.set_title('تصویر با رزولوشن کاهش یافته (4 بیتی)')
    ax2.axis('off')

    plt.tight_layout()
    plt.show()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    ax1.hist(img_array.ravel(), bins=256, range=(0, 256))
    ax1.set_title('هیستوگرام تصویر اصلی (8 بیتی)')
    ax1.set_xlabel('شدت روشنایی')
    ax1.set_ylabel('تعداد پیکسل‌ها')

    ax2.hist(img_4bit_scaled.ravel(), bins=16, range=(0, 256))
    ax2.set_title('هیستوگرام تصویر با رزولوشن کاهش یافته (4 بیتی)')
    ax2.set_xlabel('شدت روشنایی')
    ax2.set_ylabel('تعداد پیکسل‌ها')

    plt.tight_layout()
    plt.show()

reduce_brightness_resolution('image.png')