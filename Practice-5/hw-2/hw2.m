% load the image and grayscale it
originalImage = imread('eight.png');
originalImage = rgb2gray(originalImage);

% ddd  noise
noisyImage = imnoise(originalImage, 'salt & pepper', 0.03);

% sizes to test
filterSizes = [3, 5, 7];

% filtering
figure;
subplot(2, 2, 1);
imshow(noisyImage);
title('Noisy Image');

for i = 1:length(filterSizes)
    % current filter size
    filterSize = filterSizes(i);
    
    % median filtering
    medianFiltered = medfilt2(noisyImage, [filterSize, filterSize]);
    
    % mean filtering
    meanFilter = fspecial('average', [filterSize, filterSize]);
    meanFiltered = imfilter(noisyImage, meanFilter, 'symmetric');
    
    % max filtering
    maxFiltered = ordfilt2(noisyImage, filterSize^2, true(filterSize));
    
    %min filtering
    minFiltered = ordfilt2(noisyImage, 1, true(filterSize));
    
    % results
    figure;
    subplot(2, 2, 1); imshow(medianFiltered); title(['Median Filter (', num2str(filterSize), 'x', num2str(filterSize), ')']);
    subplot(2, 2, 2); imshow(meanFiltered); title(['Mean Filter (', num2str(filterSize), 'x', num2str(filterSize), ')']);
    subplot(2, 2, 3); imshow(maxFiltered); title(['Max Filter (', num2str(filterSize), 'x', num2str(filterSize), ')']);
    subplot(2, 2, 4); imshow(minFiltered); title(['Min Filter (', num2str(filterSize), 'x', num2str(filterSize), ')']);
end
