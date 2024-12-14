% load the input image
img = imread('img.png');
img = rgb2gray(img); % convert to grayscale
[m, n] = size(img); % get image size

% --- calculate input histogram and cdf ---
hist_img = imhist(img); % input histogram
pr = hist_img / (m * n); % normalize histogram to get probabilities
cdf_img = cumsum(pr); % input cdf

% --- create target histogram + cdf ---
u = 70; % mean
g = 30; % std deviation
x = 0:255; % gray level values
target_hist = exp(-((x - u).^2) / (2 * g^2)); % target function
target_hist = target_hist / sum(target_hist); % normalize target histogram
cdf_target = cumsum(target_hist); % target cdf

% ------------ histogram mapping ------------
mapping = zeros(256, 1); % empty mapping array
for k = 1:256
    [~, q] = min(abs(cdf_img(k) - cdf_target)); % find closest match
    mapping(k) = q - 1; % store mapping
end

% apply mapping to input image
output_img = mapping(double(img) + 1);

% --- calculate histogram for output image ---
hist_output = imhist(uint8(output_img)); % output histogram

% show input image
figure;
imshow(img);
title('input image');

% show input histogram
figure;
bar(0:255, hist_img, 'k');
title('input histogram');
xlabel('gray level');
ylabel('count');

% show output image
figure;
imshow(uint8(output_img));
title('output image');

% show output histogram
figure;
bar(0:255, hist_output, 'b');
title('output histogram');
xlabel('gray level');
ylabel('count');

% show target histogram
figure;
plot(0:255, target_hist, 'r', 'LineWidth', 2);
title('target histogram');
xlabel('gray level');
ylabel('probability');