% Read the image in grayscale
img = imread('aks.jpg');
gray_img = rgb2gray(img);

% Angle of rotation
theta = deg2rad(60);

% Affine transformation matrix for rotation
T = [cos(theta) -sin(theta) 0;
sin(theta) cos(theta) 0;
0 0 1];

% Apply the affine transformation to the image
tform = affine2d(T);
rotated_img = imwarp(gray_img, tform);

% Display the original and rotated images
figure;
subplot(1, 2, 1), imshow(gray_img), title('Original Image');
subplot(1, 2, 2), imshow(rotated_img), title('Rotated Image');
