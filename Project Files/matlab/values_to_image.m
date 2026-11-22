function img = values_to_image(v, shape)
% VALUES_TO_IMAGE  Rebuild an image of the given shape from values (row by row),
%   clipped to [0, 1].
img = reshape(v(1:shape(1)*shape(2)), shape(2), shape(1)).';
img = min(max(img, 0), 1);
end
