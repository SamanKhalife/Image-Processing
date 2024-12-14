% input matrix A
A = [
    12  60 191  20;
     5 185 255  15;
     0  25  79 171;
    82  51  97 132
];

% filter matrix W
W = [
    1 2 3;
    4 5 6;
    7 8 9
];

% full convolution
fullConv = conv2(A, W, 'full');

% same convolution
sameConv = conv2(A, W, 'same');

% results
disp('Full Convolution Result:');
disp(fullConv);

disp('Same Convolution Result:');
disp(sameConv);

% -------------------------------------

% normalize a matrix to range 0-255
normalizeTo255 = @(matrix) uint8(255 * (matrix - min(matrix(:))) / (max(matrix(:)) - min(matrix(:))));

% normalize the full convolution result
normalizedFullConv = normalizeTo255(fullConv);

% normalize the same convolution result
normalizedSameConv = normalizeTo255(sameConv);

% normalized results
disp('Normalized Full Convolution Result (0-255):');
disp(normalizedFullConv);

disp('Normalized Same Convolution Result (0-255):');
disp(normalizedSameConv);