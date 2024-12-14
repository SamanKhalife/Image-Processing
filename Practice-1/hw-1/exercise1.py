# برنامه ای بنویسید که عکس  سیاه و سفید blob.png را بخواند و
#  آنرا به نمایش دهد (نوع 1 و نوع 3)

from PIL import Image
import matplotlib.pyplot as plt

def display_image(image, title):
    plt.figure(figsize=(10, 5))
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

image = Image.open('blob.png')

# Display image as binary (using mode='1')
image_type1 = image.convert('1')
display_image(image_type1, 'Black and White Image (Type 1)')

# Display image as grayscale (using mode='L')
image_type3 = image.convert('L')
display_image(image_type3, 'Black and White Image (Type 3)')