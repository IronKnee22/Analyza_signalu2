import numpy as np
import pandas as pd
from scipy.io import loadmat
from scipy.signal import butter, filtfilt, welch
from scipy.stats import skew


def bandpass_filter(
    data: np.array,
    lowcut: float,
    highcut: float,
    fs: int,
    order: int = 5,
) -> np.array:
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype="band")
    return filtfilt(b, a, data)


def calculate_features(segment: np.array, fs: int) -> dict:
    frequencies, power_spectrum = welch(segment, fs, nperseg=1024)
    band_freqs = {
        "Delta": (0.5, 4),
        "Theta": (4, 8),
        "Alpha": (8, 12),
        "Beta": (12, 30),
    }
    features = {}
    for band, (low, high) in band_freqs.items():
        idx = (frequencies >= low) & (frequencies <= high)
        features[f"{band} Power"] = np.sum(power_spectrum[idx])
    features.update(
        {
            "Mean Amplitude": np.mean(segment),
            "Standard Deviation": np.std(segment),
            "Skewness": skew(segment),
            "Shannon Entropy": -np.sum(
                (power_spectrum / np.sum(power_spectrum))
                * np.log2(power_spectrum / np.sum(power_spectrum) + 1e-10),
            ),
        },
    )
    return features


def varname(prefix: str, i: int) -> str:
    return f"{prefix}0{i}" if i < 10 else f"{prefix}{i}"


def main() -> None:
    fs = 250
    data = loadmat("data/eeg.mat")
    signals = [data[varname("x", i)] for i in range(1, 11)]
    labels = [data[varname("c", i)].flatten() if i < 10 else None for i in range(1, 11)]

    for i, (x, c) in enumerate(zip(signals, labels), start=1):
        features = [
            calculate_features(bandpass_filter(x[:, j], 0.1, 30, fs), fs)
            for j in range(x.shape[1])
        ]
        df = pd.DataFrame(features)
        if c is not None:
            df["Class"] = c
        df.to_csv(f"data/features/features_subject_{i}.csv", index=False)
        print(f"Uloženo: data/features/features_subject_{i}.csv")


if __name__ == "__main__":
    main()
