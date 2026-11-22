function play_audio(x, fs)
% PLAY_AUDIO  Play x through the speakers.
sound(0.9 * x / max(abs(x)), fs);
end
