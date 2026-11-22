function [x, fs] = read_wav(path)
% READ_WAV  Read a WAV file as a mono signal in [-1, 1].
[x, fs] = audioread(path);
x = mean(x, 2);
end
