function img = read_image(path, n)
% READ_IMAGE  Read an image as an n x n grayscale array with values in [0, 1].
if nargin < 2, n = 128; end
raw = imread(path);
A = double(raw);
if size(A, 3) > 1, A = mean(A(:, :, 1:3), 3); end
if isa(raw, 'uint8'), A = A / 255;
elseif isa(raw, 'uint16'), A = A / 65535;
else, A = A / max(A(:));
end
rows = round(linspace(1, size(A, 1), n));
cols = round(linspace(1, size(A, 2), n));
img = A(rows, cols);
end
