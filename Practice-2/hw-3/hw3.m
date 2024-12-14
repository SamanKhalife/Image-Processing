% load the image
img = imread('img.png');

% convert to grayscale
img = rgb2gray(img);

% show the input image
figure;
imshow(img);
title('input image');

% show the histogram of the input image
figure;
histogram(img(:), 256);
title('input image histogram');
xlabel('pixel intensity');
ylabel('frequency');

% apply histogram equalization (increase contrast)
outputImg = histeq(img);

% show the output image (contrast enhanced)
figure;
imshow(outputImg);
title('output image (contrast enhanced)');

% show the histogram of the output image
figure;
histogram(outputImg(:), 256);
title('output image histogram');
xlabel('pixel intensity');
ylabel('frequency');
