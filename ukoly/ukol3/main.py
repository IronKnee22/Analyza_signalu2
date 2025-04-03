from copy import deepcopy

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.io import loadmat
from scipy.signal import butter, filtfilt, welch
from scipy.stats import skew

data = loadmat(r"data/eeg.mat")
x01 = data["x01"]
x02 = data["x02"]
x03 = data["x03"]
x04 = data["x04"]
x05 = data["x05"]
x06 = data["x06"]
x07 = data["x07"]
x08 = data["x08"]
x09 = data["x09"]
x10 = data["x10"]

c01 = data["c01"]

fs = 250


def bandpass_filter(
    data: np.ndarray,
    lowcut: float,
    highcut: float,
    fs: int,
    order: int = 5,
) -> np.ndarray:
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype="band")
    return filtfilt(b, a, data)


# plt.figure(figsize=(15, 10))
# for i in range(5):
#     plt.subplot(5, 1, i + 1)
#     filtered_signal = bandpass_filter(x01[:, i], 0.1, 30, fs)
#     plt.plot(filtered_signal)
#     plt.title(f"Filtrovaný segment {i + 1}")
#     plt.xlabel("Vzorky")
#     plt.ylabel("Amplituda")
# plt.tight_layout()


def calculate_features(segment: np.ndarray, fs: int) -> dict:
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


features_results = [
    calculate_features(bandpass_filter(x01[:, i], 0.1, 30, fs), fs)
    for i in range(x01.shape[1])
]
features_df = pd.DataFrame(features_results)
print(features_df.head())

features_results_2 = [
    calculate_features(bandpass_filter(x02[:, i], 0.1, 30, fs), fs)
    for i in range(x02.shape[1])
]
features_results_3 = [
    calculate_features(bandpass_filter(x03[:, i], 0.1, 30, fs), fs)
    for i in range(x03.shape[1])
]
features_results_4 = [
    calculate_features(bandpass_filter(x04[:, i], 0.1, 30, fs), fs)
    for i in range(x04.shape[1])
]
features_results_5 = [
    calculate_features(bandpass_filter(x05[:, i], 0.1, 30, fs), fs)
    for i in range(x05.shape[1])
]
features_results_6 = [
    calculate_features(bandpass_filter(x06[:, i], 0.1, 30, fs), fs)
    for i in range(x06.shape[1])
]
features_results_7 = [
    calculate_features(bandpass_filter(x07[:, i], 0.1, 30, fs), fs)
    for i in range(x07.shape[1])
]
features_results_8 = [
    calculate_features(bandpass_filter(x08[:, i], 0.1, 30, fs), fs)
    for i in range(x08.shape[1])
]
features_results_9 = [
    calculate_features(bandpass_filter(x09[:, i], 0.1, 30, fs), fs)
    for i in range(x09.shape[1])
]
features_results_10 = [
    calculate_features(bandpass_filter(x10[:, i], 0.1, 30, fs), fs)
    for i in range(x10.shape[1])
]

class_labels = data["c01"]
class_labels = class_labels.flatten()

features_df_class = deepcopy(features_df)
features_df_class["Class"] = class_labels
print(features_df_class.head())


plt.figure(figsize=(12, 10))
for i, feature in enumerate(
    features_df.columns,
):
    plt.subplot(4, 2, i + 1)
    sns.boxplot(x="Class", y=feature, data=features_df_class)
    plt.title(feature)
plt.tight_layout()
plt.savefig("feature_boxplots.pdf")
plt.show()


plt.show()
pass
