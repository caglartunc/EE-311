function [y, fs_new] = lower_rate(x, fs, D)
% LOWER_RATE  Sample x at the lower rate fs/D by keeping every D-th sample.
y = x(1:D:end);
fs_new = fs / D;
end
