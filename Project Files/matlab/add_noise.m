function [y, w] = add_noise(x, snr_db, seed)
% ADD_NOISE  Add white Gaussian noise to x at the given SNR (dB).
%   SNR = average power of x / noise variance. Returns noisy signal and noise.
if nargin > 2, rng(seed); end
sigma = sqrt(mean(x.^2) / 10^(snr_db/10));
w = sigma * randn(size(x));
y = x + w;
end
