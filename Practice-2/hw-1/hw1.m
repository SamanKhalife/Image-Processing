% load the image
image = imread('dollar.png');

% make it grayscale
image = rgb2gray(image);

figure;
for bit = 1:8
    % get the bit plane
    bitPlane = bitget(image, bit);
    % place in subplot
    subplot(2, 4, bit);
    % convert the bit plane from 0 and 1 to binary image
    imshow(logical(bitPlane));
    % label it
    title(['bit plane ' num2str(bit)]);
end
