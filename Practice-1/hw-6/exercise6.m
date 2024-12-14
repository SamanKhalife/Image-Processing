# کنتراست را تعریف کنید و معیاری مناسب برای کنتراست تصویر در متلب ارائه دهید


function contrast = measureImageContrast(image)
    if size(image, 3) == 3
        grayImage = rgb2gray(image);
    else
        grayImage = image;
    end

    grayImage = im2double(grayImage);

    meanIntensity = mean(grayImage(:));

    stdIntensity = std(grayImage(:));

    contrast = stdIntensity / meanIntensity;

    fprintf('میانگین روشنایی: %.4f\n', meanIntensity);
    fprintf('انحراف استاندارد روشنایی: %.4f\n', stdIntensity);
    fprintf('کنتراست (ضریب تغییرات): %.4f\n', contrast);

    figure;
    imhist(grayImage);
    title('هیستوگرام تصویر');
    xlabel('شدت روشنایی');
    ylabel('تعداد پیکسل‌ها');
end

% مثال استفاده
% img = imread('your_image.jpg');
% contrast = measureImageContrast(img);