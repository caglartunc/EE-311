# EE311 Term Project, Fall 2026: provided tools

Python: `ee311_tools.py` (use `from ee311_tools import *`). Needs numpy, scipy, matplotlib, Pillow; `sounddevice` only for `play_audio`.
MATLAB: one `.m` file per function in `matlab/`. Needs the Signal Processing Toolbox.

Names and arguments are the same in both languages. Frequencies are in Hz.

| Function | What it does |
| --- | --- |
| `ctft(x, fs)` | Approximate CTFT of a sampled signal; returns `f` and `X` |
| `make_filter(fs, kind, fc, order, Q)` | Ready-made filter: `'lowpass'`, `'highpass'`, `'bandpass'` (`fc = [f1, f2]`) or `'notch'` (`fc = f0`). Higher `order`: sharper edge. Higher `Q`: narrower notch |
| `apply_filter(b, a, x)` | Passes `x` through the filter |
| `freq_response(b, a, f, fs)` | Complex frequency response of the filter at frequencies `f` |
| `lin_chirp(t, f1, f2, T)` | Linear chirp from `f1` to `f2` over `T` seconds |
| `add_noise(x, snr_db, seed)` | Adds white Gaussian noise at the given SNR |
| `scale_noise(x, n, snr_db)` | Scales a recorded noise `n` to the given SNR and adds it |
| `ct_convolve(x, h, fs)` | Convolution integral of two sampled signals; output starts at the sum of the two start times |
| `lower_rate(x, fs, D)` | Samples at the lower rate `fs/D` (keeps every `D`-th sample) |
| `impulse_train(s, D)` | Places samples `s` as an impulse train on the original fine grid |
| `zero_order_hold(s, D)` | Holds each sample of `s` for `D` points on the fine grid |
| `sample_autocorr(x, fs, max_lag)` | Sample autocorrelation for lags up to `max_lag` seconds |
| `read_wav`, `write_wav`, `play_audio` | Audio input and output |
| `read_image(path, n)`, `show_image(img)` | Read an image as an n x n grayscale array in [0, 1]; display it |
| `image_to_pulses(img, sps)` | Image read row by row, each pixel a rectangular pulse of `sps` samples |
| `pulses_to_values(y, sps)` | One value per pulse (average of the second half of each pulse) |
| `values_to_image(v, shape)` | Rebuilds an image from values, clipped to [0, 1] |
| `image_psnr(ref, est)` | PSNR in dB between two images |
