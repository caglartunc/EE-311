function show_image(img, ttl)
% SHOW_IMAGE  Display a grayscale image with values in [0, 1].
if nargin < 2, ttl = ''; end
imagesc(img, [0 1]); colormap(gray); axis image off; title(ttl);
end
