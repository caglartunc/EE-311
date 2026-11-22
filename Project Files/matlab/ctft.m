function [f, X] = ctft(x, fs)
% CTFT  Approximate CTFT of a signal sampled at fs (Hz).
%   [f, X] = ctft(x, fs) returns frequencies f (Hz) and complex X(f).
x = x(:).';
N = length(x);
X = fftshift(fft(x)) / fs;
f = (-floor(N/2):ceil(N/2)-1) * fs / N;
end
