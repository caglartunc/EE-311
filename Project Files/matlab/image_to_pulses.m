function m = image_to_pulses(img, sps)
% IMAGE_TO_PULSES  Read the image row by row; each pixel value becomes a
%   rectangular pulse of sps samples. Returns the message signal m.
v = reshape(img.', [], 1);
m = repelem(v, sps);
end
