function y = ct_convolve(x, h, fs)
% CT_CONVOLVE  Convolution integral of two signals sampled at fs (Hz).
%   If x starts at time t_x and h at time t_h, the output starts at t_x + t_h.
y = conv(x(:), h(:)) / fs;
end
