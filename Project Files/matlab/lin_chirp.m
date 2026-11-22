function y = lin_chirp(t, f1, f2, T)
% LIN_CHIRP  Linear chirp whose frequency goes from f1 to f2 (Hz) over T seconds.
y = cos(2*pi*(f1*t + (f2 - f1)/(2*T)*t.^2));
end
