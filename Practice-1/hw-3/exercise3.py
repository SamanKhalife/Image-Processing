# برنامه ای بنویسید که عکس  pappers.png را بخواند ان را نمایش دهد

from PIL import Image
import matplotlib.pyplot as plt

def display_image(image, title):
    plt.figure(figsize=(10, 8))
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

image = Image.open('pappers.png')

# Convert the image to Type 1 (binary)
image_binary = image.convert('1')

display_image(image_binary, 'pappers.png as Binary (Type 1)')

print(f"Image dimensions: {image_binary.size}")
print(f"Image format: {image_binary.format}")
print(f"Image mode: {image_binary.mode}")