"""EE311 Term Project, Fall 2026: provided tools.

Import with:  from ee311_tools import *
Requires numpy, scipy, matplotlib (and sounddevice only for play()).
"""
import numpy as np
from scipy import signal
from scipy.io import wavfile


# ---------------------------------------------------------------- spectra
def ctft(x, fs):
    """Approximate CTFT of a signal sampled at fs (Hz).
    Returns frequencies f (Hz) and complex X(f)."""
    x = np.asarray(x, float)
    N = len(x)
    X = np.fft.fftshift(np.fft.fft(x)) / fs
    f = np.fft.fftshift(np.fft.fftfreq(N, d=1 / fs))
    return f, X


# ---------------------------------------------------------------- filters
def make_filter(fs, kind, fc, order=4, Q=10):
    """Ready-made filter for a signal sampled at fs (Hz).
    kind: 'lowpass', 'highpass', 'bandpass' (fc = [f1, f2]) or 'notch' (fc = f0).
    order: sharpness of lowpass/highpass/bandpass. Q: narrowness of the notch.
    Returns (b, a), used by apply_filter and freq_response."""
    if kind == 'notch':
        return signal.iirnotch(fc, Q, fs=fs)
    if kind not in ('lowpass', 'highpass', 'bandpass'):
        raise ValueError("kind must be 'lowpass', 'highpass', 'bandpass' or 'notch'")
    return signal.butter(order, fc, btype=kind, fs=fs)


def apply_filter(b, a, x):
    """Pass signal x through the filter (b, a)."""
    return signal.lfilter(b, a, np.asarray(x, float))


def freq_response(b, a, f, fs):
    """Complex frequency response H(f) of filter (b, a) at frequencies f (Hz)."""
    _, H = signal.freqz(b, a, worN=np.asarray(f, float), fs=fs)
    return H


# ---------------------------------------------------------------- signals
def lin_chirp(t, f1, f2, T):
    """Linear chirp whose frequency goes from f1 to f2 (Hz) over T seconds."""
    t = np.asarray(t, float)
    return np.cos(2 * np.pi * (f1 * t + (f2 - f1) / (2 * T) * t ** 2))


def add_noise(x, snr_db, seed=None):
    """Add white Gaussian noise to x at the given SNR (dB).
    SNR = average power of x / noise variance. Returns (noisy signal, noise)."""
    x = np.asarray(x, float)
    rng = np.random.default_rng(seed)
    sigma = np.sqrt(np.mean(x ** 2) / 10 ** (snr_db / 10))
    w = sigma * rng.standard_normal(len(x))
    return x + w, w


def scale_noise(x, n, snr_db):
    """Scale a recorded noise signal n so that x + n has the given SNR (dB).
    Returns (noisy signal, scaled noise)."""
    x = np.asarray(x, float)
    n = np.asarray(n, float)
    c = np.sqrt(np.mean(x ** 2) / (np.mean(n ** 2) * 10 ** (snr_db / 10)))
    return x + c * n, c * n


def ct_convolve(x, h, fs):
    """Convolution integral of two signals sampled at fs (Hz).
    If x starts at time t_x and h at time t_h, the output starts at t_x + t_h."""
    return np.convolve(np.asarray(x, float), np.asarray(h, float)) / fs


def lower_rate(x, fs, D):
    """Sample x at the lower rate fs/D by keeping every D-th sample.
    Returns (new signal, new rate)."""
    return np.asarray(x)[::D], fs / D


def impulse_train(samples, D):
    """Impulse-train signal on the original fine grid: each sample (scaled by D)
    at its sampling instant, zeros in between. Use with a lowpass for reconstruction."""
    xp = np.zeros(len(samples) * D)
    xp[::D] = D * np.asarray(samples, float)
    return xp


def zero_order_hold(samples, D):
    """Zero-order hold on the original fine grid: each sample held for D points."""
    return np.repeat(np.asarray(samples, float), D)


def sample_autocorr(x, fs, max_lag):
    """Sample autocorrelation R(tau) = (1/N) sum x[n] x[n+m] for |tau| <= max_lag (s).
    Returns lags (s) and R."""
    x = np.asarray(x, float)
    N = len(x)
    R = signal.correlate(x, x, mode='full', method='fft') / N
    m = np.arange(-(N - 1), N)
    keep = np.abs(m) <= int(round(max_lag * fs))
    return m[keep] / fs, R[keep]


# ---------------------------------------------------------------- audio
def read_wav(path):
    """Read a WAV file. Returns (x, fs) with x mono and scaled to [-1, 1]."""
    fs, raw = wavfile.read(path)
    x = raw.astype(float)
    if np.issubdtype(raw.dtype, np.integer):
        x = x / float(np.iinfo(raw.dtype).max + 1)
    if x.ndim > 1:
        x = x.mean(axis=1)
    return x, fs


def write_wav(path, x, fs):
    """Write x to a 16-bit WAV file, scaled so its peak is 0.9."""
    x = np.asarray(x, float)
    x = 0.9 * x / max(np.max(np.abs(x)), 1e-12)
    wavfile.write(path, int(fs), (x * 32767).astype(np.int16))


def play_audio(x, fs):
    """Play x through the speakers (needs: pip install sounddevice)."""
    import sounddevice as sd
    x = np.asarray(x, float)
    sd.play(0.9 * x / max(np.max(np.abs(x)), 1e-12), int(fs))
    sd.wait()


# ---------------------------------------------------------------- images and pulses
def read_image(path, n=128):
    """Read an image as an n x n grayscale array with values in [0, 1]."""
    from PIL import Image
    img = Image.open(path).convert('L').resize((n, n))
    return np.asarray(img, float) / 255.0


def show_image(img, title=''):
    """Display a grayscale image with values in [0, 1]."""
    import matplotlib.pyplot as plt
    plt.imshow(img, cmap='gray', vmin=0, vmax=1)
    plt.title(title)
    plt.axis('off')


def image_to_pulses(img, sps):
    """Read the image row by row; each pixel value becomes a rectangular pulse
    of sps samples. Returns the message signal m."""
    return np.repeat(np.asarray(img, float).flatten(), sps)


def pulses_to_values(y, sps):
    """One value per pulse: the average of the second half of each pulse."""
    y = np.asarray(y, float)
    K = len(y) // sps
    return y[:K * sps].reshape(K, sps)[:, sps // 2:].mean(axis=1)


def values_to_image(v, shape):
    """Rebuild an image of the given shape from values (row by row), clipped to [0, 1]."""
    return np.clip(np.asarray(v, float)[:shape[0] * shape[1]].reshape(shape), 0, 1)


def image_psnr(ref, est):
    """PSNR in dB between two images with values in [0, 1]."""
    mse = np.mean((np.asarray(ref, float) - np.asarray(est, float)) ** 2)
    return 10 * np.log10(1 / max(mse, 1e-12))
