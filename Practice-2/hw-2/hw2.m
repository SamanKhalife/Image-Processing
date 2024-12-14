% load the image
image = imread('tire.png');

% make it grayscale
image = rgb2gray(image);
figure;
% inamge(:) converts 2d image into 1d
histogram(image(:), 256);
title('histogram');
xlabel('pixel intensity');
ylabel('pixel count');
pixelCounts = imhist(image); % get histogram in vector format from 0 to 255
pdf = pixelCounts / numel(image); % devide each element of the vector to the total amount of pixels

figure;
plot(0:255, pdf, 'LineWidth', 2);
title('pdf');
xlabel('pixel intensity');
ylabel('probability');
