import numpy as np
import matplotlib.pyplot as plt
import scipy.io
from scipy.interpolate import PchipInterpolator
from scipy.signal import butter, filtfilt

def butter_lowpass_filter(data, cutoff, fs, order=3):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low')
    return filtfilt(b, a, data)

def baseline_iteration(signal, t, fs, cutoff, lower_thresh, upper_thresh):
    baseline = butter_lowpass_filter(signal, cutoff=cutoff, fs=fs, order=3)
    
    mask = (signal >= baseline - lower_thresh) & (signal <= baseline + upper_thresh)
    signal_cut = np.full_like(signal, np.nan)
    signal_cut[mask] = signal[mask]

    valid_idx = ~np.isnan(signal_cut)
    pchip = PchipInterpolator(t[valid_idx], signal_cut[valid_idx])
    signal_interp = signal_cut.copy()
    signal_interp[np.isnan(signal_cut)] = pchip(t[np.isnan(signal_cut)])
    
    return signal_interp, baseline

def detect_advanced_decelerations(signal, baseline, fs):
    under_5 = signal < (baseline - 5)
    under_10 = signal < (baseline - 10)
    between_5_10 = (signal >= (baseline - 10)) & (signal < (baseline - 5))
    
    decel_regions = []
    i = 0
    while i < len(signal):
        if under_10[i]:
            start = i
            # Hledáme konec podle tří možných kritérií
            while i < len(signal):
                if signal[i] > baseline[i]:  # překročil baseline
                    break
                elif all(under_5[i:i+40]):  # 10s pod 5 bpm
                    i += 40
                    break
                elif all(between_5_10[i:i+72]):  # 18s mezi 5-10 bpm
                    i += 72
                    break
                i += 1
            end = i
            if end - start >= fs * 15:  # 15s trvání
                decel_regions.append((start, end))
        i += 1
    return decel_regions

def remove_regions(signal, regions):
    signal_cleaned = signal.copy()
    for start, end in regions:
        signal_cleaned[start:end] = 0
    return signal_cleaned



def detect_accel_and_decel(signal, baseline, fs):
    min_len_samples = int(15 * fs)
    accel_regions = []
    decel_regions = []

    # --- Akcelerace ---
    above_10 = signal > (baseline + 10)
    i = 0
    while i < len(signal):
        if above_10[i]:
            start = i
            while i < len(signal) and above_10[i]:
                i += 1
            end = i
            if end - start >= min_len_samples:
                accel_regions.append((start, end))
        else:
            i += 1

    # --- Decelerace ---
    under_5 = signal < (baseline - 5)
    under_10 = signal < (baseline - 10)
    between_5_10 = (signal >= (baseline - 10)) & (signal < (baseline - 5))

    i = 0
    while i < len(signal):
        if under_10[i]:
            start = i
            while i < len(signal):
                if signal[i] > baseline[i]:  # překročí baseline
                    break
                elif all(under_5[i:i+40]):  # 10s pod 5 bpm
                    i += 40
                    break
                elif all(between_5_10[i:i+72]):  # 18s mezi 5–10 bpm
                    i += 72
                    break
                i += 1
            end = i
            if end - start >= min_len_samples:
                decel_regions.append((start, end))
        i += 1

    return accel_regions, decel_regions

# === Načtení a interpolace ===
mat = scipy.io.loadmat(r'data/data_FHR.mat')
fhr = mat['fhr'][:, 0].astype(float)

fhr_nan = fhr.copy()
fhr_nan[fhr_nan == 0] = np.nan

fs = 4  # Hz
t = np.arange(len(fhr_nan)) / fs 

valid_idx = ~np.isnan(fhr_nan)
nan_idx = np.isnan(fhr_nan)

pchip = PchipInterpolator(t[valid_idx], fhr_nan[valid_idx])
fhr_interp = fhr_nan.copy()
fhr_interp[nan_idx] = pchip(t[nan_idx])

# === Iterace baseline ===
iterations = []
filtered_signals = []

s1, b1 = baseline_iteration(fhr_interp, t, fs, cutoff=0.008, lower_thresh=5, upper_thresh=5)
iterations.append(b1)
filtered_signals.append(s1)

s2, b2 = baseline_iteration(s1, t, fs, cutoff=0.006, lower_thresh=5, upper_thresh=5)
iterations.append(b2)
filtered_signals.append(s2)

s3, b3 = baseline_iteration(s2, t, fs, cutoff=0.006, lower_thresh=5, upper_thresh=5)
iterations.append(b3)
filtered_signals.append(s3)

s4, b4 = baseline_iteration(s3, t, fs, cutoff=0.006, lower_thresh=10, upper_thresh=5)
iterations.append(b4)
filtered_signals.append(s4)


plt.figure()

plt.subplot(2, 1, 1)
plt.plot(t, fhr)
plt.title("Původní FHR signál")

plt.subplot(2, 1, 2)
plt.plot(t, fhr, label='Původní')
plt.plot(t, fhr_interp, color='red', label='Interpolovaný')
plt.title("Interpolace chybějících hodnot")
plt.legend()

plt.tight_layout()


plt.figure()
plt.plot(t, fhr_interp, label='Interpolovaný FHR', color='lightgray', linewidth=1)

colors = ['blue', 'green', 'orange', 'red']
for i, b in enumerate(iterations):
    plt.plot(t, b, label=f'Baseline iterace {i+1}', color=colors[i], linewidth=1.5)

plt.xlabel('Čas [s]')
plt.ylabel('Frekvence [bpm]')
plt.title('Iterativní odhad baseline (Taylor)')
plt.legend()
plt.grid(True)
plt.tight_layout()



num_signals = len(filtered_signals)
signals_per_figure = 4

for fig_index in range(0, num_signals, signals_per_figure):
    fig, axs = plt.subplots(4, 1, figsize=(14, 12), sharex=True)
    fig.suptitle(f'Původní signály s baseline a značkami (signály {fig_index}–{fig_index + signals_per_figure - 1})', fontsize=16)

    for i in range(signals_per_figure):
        idx = fig_index + i
        if idx >= num_signals:
            break

        signal = filtered_signals[idx]
        baseline = iterations[idx]
        accel_regions, decel_regions = detect_accel_and_decel(fhr_interp, baseline, fs)

        ax = axs[i]
        ax.plot(t, signal, label='FHR', color='black', alpha=0.6)
        ax.plot(t, baseline, label='Baseline', color='red')

        for start, _ in accel_regions:
            ax.plot(t[start], baseline[start], '^', color='green', label='Akcelerace' if start == accel_regions[0][0] else "")
        for start, _ in decel_regions:
            ax.plot(t[start], baseline[start], 'v', color='blue', label='Decelerace' if start == decel_regions[0][0] else "")

        ax.set_title(f'Signál {idx}')
        ax.legend(loc='upper right')
        ax.grid(True)

for fig_index in range(0, num_signals, signals_per_figure):
    fig1, axs1 = plt.subplots(4, 1, figsize=(14, 12), sharex=True)
    fig2, axs2 = plt.subplots(4, 1, figsize=(14, 12), sharex=True)

    for i in range(signals_per_figure):
        idx = fig_index + i
        if idx >= num_signals:
            break

        signal = filtered_signals[idx]
        baseline = iterations[idx]
        accel_regions, decel_regions = detect_accel_and_decel(fhr_interp, baseline, fs)
        cleaned_signal = remove_regions(signal, accel_regions + decel_regions)

        # Původní signál
        ax1 = axs1[i]
        ax1.plot(t, signal, label='FHR', color='black', alpha=0.6)
        ax1.plot(t, baseline, label='Baseline', color='red')

        for start, _ in accel_regions:
            ax1.plot(t[start], baseline[start], '^', color='green', label='Akcelerace' if start == accel_regions[0][0] else "")
        for start, _ in decel_regions:
            ax1.plot(t[start], baseline[start], 'v', color='blue', label='Decelerace' if start == decel_regions[0][0] else "")

        ax1.set_title(f'Iterace {idx+1}')
        ax1.legend(loc='upper right')
        ax1.grid(True)

        # Očištěný signál
        ax2 = axs2[i]
        ax2.plot(t, signal, label='Původní signál', color='gray', alpha=0.6)
        ax2.plot(t, cleaned_signal, label='Bez akcelerací/decelerací', color='black')
        ax2.plot(t, baseline, label='Baseline', color='red')

        for start, _ in accel_regions:
            ax2.plot(t[start], baseline[start], '^', color='green', label='Akcelerace' if start == accel_regions[0][0] else "")
        for start, _ in decel_regions:
            ax2.plot(t[start], baseline[start], 'v', color='blue', label='Decelerace' if start == decel_regions[0][0] else "")

        ax2.set_title(f'Iterace {idx+1}')
        ax2.legend(loc='upper right')
        ax2.grid(True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()

# TODO: figure 2 se rozmyslet ale podle mě může jít klidně pryč
# TODO: dát to nějak hezky do funkcí protože je potřeba aby se to provedlo celé ještě 3
# TODO: Nakonec tam musím hodit ještě nějakou diskuzi
