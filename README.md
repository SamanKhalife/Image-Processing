# Image-Processing-Uni

This Python-based image processing tool applies several image enhancement algorithms, such as sharpening, noise removal, histogram equalization, color enhancement, and brightness/contrast adjustment.

## Features
- **Image Sharpening**: Enhances image details using a custom kernel.
- **Median Blur**: Reduces noise in the image using a median filter.
- **Histogram Equalization**: Improves contrast in grayscale images.
- **Color Enhancement**: Enhances the hue, saturation, and value (HSV) of the image.
- **Brightness and Contrast Adjustment**: Modifies brightness and contrast using a scaling factor and offset.

## Algorithms

1. **Image Sharpening**:
   - A custom convolution kernel is used to sharpen the image by emphasizing edges and fine details.
   - Kernel used:
   ```python
   kernel = np.array([[0, -3, 0], [-3, 15, -3], [0, -3, 0]])
   ```

2. **Median Blur**:
   - A median filter is applied to reduce noise by replacing each pixel with the median of its neighboring pixels. This helps smooth the image without blurring the edges.

3. **Histogram Equalization**:
   - Enhances the contrast of the image by spreading out the intensity distribution (used on grayscale images). This makes the features of the image more distinguishable.

4. **Color Enhancement**:
   - The image is converted to the HSV color space, and then the hue, saturation, and value are each increased by a factor of 1.2, improving the vibrancy of the image.

5. **Brightness and Contrast Adjustment**:
   - Brightness and contrast are adjusted using the formula:
   ```python
   g(i,j) = α ⋅ f(i,j) + β
   ```
   - `α` controls contrast, while `β` adjusts brightness.

## Installation

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/yourusername/image-processing-uni.git
   cd image-processing-uni
   ```

2. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use

The tool supports both single image processing and batch processing of images from a folder.

1. **Single Image Processing**:
   ```bash
   python boom.py --input sample.jpg --output ./processed
   ```

2. **Batch Processing from Folder**:
   ```bash
   python boom.py --input ./images --output ./processed
   ```

### Command-Line Interface (CLI) Options:

- `--input <image-file-path>`: Specify the image file or folder to process.
- `--output <output-path>` (optional): Specify the output folder for processed images. If not specified, it will save the images in the current directory.

Example with output folder:
```bash
python process_image.py --input sample.jpg --output ./processed
```

## Example Output

For each image processed, the tool will generate several output files based on the applied algorithms:
- `sample_sharpened.jpg`
- `sample_median_blur.jpg`
- `sample_equalized.jpg`
- `sample_enhanced_coloured.jpg`
- `sample_brightness_contrast.jpg`

These processed images will be saved either in the current directory or in the specified output folder.