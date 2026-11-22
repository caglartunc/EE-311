function xp = impulse_train(s, D)
% IMPULSE_TRAIN  Impulse-train signal on the original fine grid: each sample
%   (scaled by D) at its sampling instant, zeros in between.
xp = zeros(numel(s)*D, 1);
xp(1:D:end) = D * s(:);
end
