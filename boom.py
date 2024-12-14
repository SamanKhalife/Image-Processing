import cv2
import numpy as np
import os
import argparse

# Function to perform all image processing tasks
def process_image(image_path, output_dir):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to load {image_path}")
        return
    base_name = os.path.basename(image_path)
    name, ext = os.path.splitext(base_name)

    # --- 1. Sharpening ---
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened_image = cv2.filter2D(image, -1, kernel)
    cv2.imwrite(os.path.join(output_dir, f'{name}_sharpened{ext}'), sharpened_image)

    # --- 2. Median Blur (Noise Removal) ---
    filtered_image = cv2.medianBlur(image, 11)
    cv2.imwrite(os.path.join(output_dir, f'{name}_median_blur{ext}'), filtered_image)

    # --- 3. Histogram Equalization (Grayscale) ---
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    equalized_image = cv2.equalizeHist(gray_image)
    cv2.imwrite(os.path.join(output_dir, f'{name}_equalized{ext}'), equalized_image)

    # --- 4. Color Enhancement (HSV Adjustment) ---
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv_image[:, :, 0] = hsv_image[:, :, 0] * 1.2
    hsv_image[:, :, 1] = hsv_image[:, :, 1] * 1.2
    hsv_image[:, :, 2] = hsv_image[:, :, 2] * 1.2
    enhanced_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
    cv2.imwrite(os.path.join(output_dir, f'{name}_enhanced_coloured{ext}'), enhanced_image)

    # --- 5. Brightness and Contrast Adjustment ---
    alpha = 2.5  # Contrast control
    beta = 100   # Brightness control
    contrast_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    cv2.imwrite(os.path.join(output_dir, f'{name}_brightness_contrast{ext}'), contrast_image)

    print(f"Processed and saved outputs for {image_path} in {output_dir}")

# CLI to process single image or folder of images
def main():
    parser = argparse.ArgumentParser(description="Process images with sharpening, noise removal, equalization, color enhancement, and brightness/contrast adjustment.")
    parser.add_argument('--input', required=True, help="Path to the input image or folder of images")
    parser.add_argument('--output', required=True, help="Path to the output directory")

    args = parser.parse_args()

    # Ensure output directory exists
    if not os.path.exists(args.output):
        os.makedirs(args.output)

    # Check if input is a file or directory
    if os.path.isfile(args.input):
        process_image(args.input, args.output)
    elif os.path.isdir(args.input):
        # Process all images in the directory
        for filename in os.listdir(args.input):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                process_image(os.path.join(args.input, filename), args.output)
    else:
        print("Input is neither a file nor a directory.")

if __name__ == '__main__':
    main()
