function H = freq_response(b, a, f, fs)
% FREQ_RESPONSE  Complex frequency response H(f) of filter [b, a] at frequencies f (Hz).
H = freqz(b, a, f(:), fs);
end
