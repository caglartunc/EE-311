function [y, ns] = scale_noise(x, n, snr_db)
% SCALE_NOISE  Scale a recorded noise signal n so that x + n has the given SNR (dB).
%   Returns noisy signal and scaled noise. x and n must have the same size.
c = sqrt(mean(x.^2) / (mean(n.^2) * 10^(snr_db/10)));
ns = c * n;
y = x + ns;
end
