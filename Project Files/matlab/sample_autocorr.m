function [lags, R] = sample_autocorr(x, fs, max_lag)
% SAMPLE_AUTOCORR  R(tau) = (1/N) sum x[n] x[n+m] for |tau| <= max_lag (s).
%   Returns lags (s) and R.
M = round(max_lag * fs);
R = xcorr(x(:), M, 'biased');
lags = (-M:M).' / fs;
end
