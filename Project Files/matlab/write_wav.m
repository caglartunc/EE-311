function write_wav(path, x, fs)
% WRITE_WAV  Write x to a 16-bit WAV file, scaled so its peak is 0.9.
audiowrite(path, 0.9 * x / max(abs(x)), fs);
end
