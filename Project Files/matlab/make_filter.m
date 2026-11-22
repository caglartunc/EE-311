function [b, a] = make_filter(fs, kind, fc, order, Q)
% MAKE_FILTER  Ready-made filter for a signal sampled at fs (Hz).
%   kind: 'lowpass', 'highpass', 'bandpass' (fc = [f1 f2]) or 'notch' (fc = f0).
%   order: sharpness of lowpass/highpass/bandpass (default 4).
%   Q: narrowness of the notch (default 10).
%   Returns [b, a], used by apply_filter and freq_response.
if nargin < 4 || isempty(order), order = 4; end
if nargin < 5 || isempty(Q), Q = 10; end
switch kind
    case 'notch'
        w0 = 2*fs*tan(pi*fc/fs);
        [b, a] = bilinear([1 0 w0^2], [1 w0/Q w0^2], fs);
    case 'lowpass'
        [b, a] = butter(order, fc/(fs/2), 'low');
    case 'highpass'
        [b, a] = butter(order, fc/(fs/2), 'high');
    case 'bandpass'
        [b, a] = butter(order, fc/(fs/2), 'bandpass');
    otherwise
        error('kind must be lowpass, highpass, bandpass or notch');
end
end
