# برنامه ای بنویسید که عکس با مقیاس خاکستری (عکس زیر)
#  را بخواند و آنرا به سه صورت   نمایش دهد (نوع 1، نوع 2 و نوع 3)


from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def display_images(images, titles):
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    for ax, img, title in zip(axs, images, titles):
        ax.imshow(img, cmap='gray')
        ax.set_title(title)
        ax.axis('off')
    plt.tight_layout()
    plt.show()

image = Image.open('Image.png').convert('L')
image_array = np.array(image)

# Type 1: Convert to binary (black and white)
image_type1 = image.convert('1')

# Type 2: Use thresholding
threshold = 128
image_type2 = ((image_array > threshold) * 255).astype(np.uint8)

# Type 3: Grayscale (original)
image_type3 = image_array

display_images([image_type1, image_type2, image_type3],
               ['Type 1 (Binary)', 'Type 2 (Threshold)', 'Type 3 (Grayscale)'])

print("Pixel values in Type 1:", np.unique(np.array(image_type1)))
print("Pixel values in Type 2:", np.unique(image_type2))
print("Pixel value range in Type 3:", image_type3.min(), "to", image_type3.max())