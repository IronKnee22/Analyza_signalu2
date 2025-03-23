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
            
            while i < len(signal):
                if signal[i] > baseline[i]:  
                    break
                elif all(under_5[i:i+40]):  
                    i += 40
                    break
                elif all(between_5_10[i:i+72]):  
                    i += 72
                    break
                i += 1
            end = i
            if end - start >= fs * 15:  
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

    
    under_5 = signal < (baseline - 5)
    under_10 = signal < (baseline - 10)
    between_5_10 = (signal >= (baseline - 10)) & (signal < (baseline - 5))

    i = 0
    while i < len(signal):
        if under_10[i]:
            start = i
            while i < len(signal):
                if signal[i] > baseline[i]:  
                    break
                elif all(under_5[i:i+40]):  
                    i += 40
                    break
                elif all(between_5_10[i:i+72]):  
                    i += 72
                    break
                i += 1
            end = i
            if end - start >= min_len_samples:
                decel_regions.append((start, end))
        i += 1

    return accel_regions, decel_regions

def interpolace(fhr_nan,t):
    valid_idx = ~np.isnan(fhr_nan)
    nan_idx = np.isnan(fhr_nan)

    pchip = PchipInterpolator(t[valid_idx], fhr_nan[valid_idx])
    fhr_interp = fhr_nan.copy()
    fhr_interp[nan_idx] = pchip(t[nan_idx])
    return fhr_interp

def baseline(fhr_interp, t, fs):
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
    return iterations, filtered_signals

def plots_akce_deakce(t, fhr, fhr_interp, iterations, filtered_signals, fs):
    plt.figure(figsize=(12, 6))
    
    # 1. Původní signál
    plt.subplot(2, 1, 1)
    plt.plot(t, fhr, color='black')
    plt.title("Původní FHR signál")
    plt.xlabel("Čas [s]")
    plt.ylabel("Frekvence [bpm]")
    plt.grid(True)

    # 2. Interpolace
    plt.subplot(2, 1, 2)
    plt.plot(t, fhr, label='Původní', color='gray')
    plt.plot(t, fhr_interp, color='red', label='Interpolovaný')
    plt.title("Interpolace chybějících hodnot ve FHR signálu")
    plt.xlabel("Čas [s]")
    plt.ylabel("Frekvence [bpm]")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # 3. Iterace baseline
    plt.figure(figsize=(14, 6))
    plt.plot(t, fhr_interp, label='Interpolovaný FHR', color='lightgray', linewidth=1)

    colors = ['blue', 'green', 'orange', 'red']
    for i, b in enumerate(iterations):
        plt.plot(t, b, label=f'Baseline - Iterace {i+1}', color=colors[i], linewidth=1.5)

    plt.title("Iterativní odhad baseline dle Taylorovy metody")
    plt.xlabel("Čas [s]")
    plt.ylabel("Frekvence [bpm]")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # 4. Akcelerace/decelerace a očištěný signál
    num_signals = len(filtered_signals)
    signals_per_figure = 4

    for fig_index in range(0, num_signals, signals_per_figure):
        fig1, axs1 = plt.subplots(4, 1, figsize=(14, 12), sharex=True)
        fig2, axs2 = plt.subplots(4, 1, figsize=(14, 12), sharex=True)

        for i in range(signals_per_figure):
            idx = fig_index + i
            if idx >= num_signals:
                break

            baseline = iterations[idx]
            accel_regions, decel_regions = detect_accel_and_decel(fhr_interp, baseline, fs)
            cleaned_signal = remove_regions(fhr_interp, accel_regions + decel_regions)

            # Graf 1: Detekce akcelerací a decelerací
            ax1 = axs1[i]
            ax1.plot(t, fhr_interp, label='FHR', color='black', alpha=0.6)
            ax1.plot(t, baseline, label='Baseline', color='red', linewidth=1)

            for j, (start, _) in enumerate(accel_regions):
                ax1.plot(t[start], baseline[start], '^', color='green', label='Akcelerace' if j == 0 else "")
            for j, (start, _) in enumerate(decel_regions):
                ax1.plot(t[start], baseline[start], 'v', color='blue', label='Decelerace' if j == 0 else "")

            ax1.set_title(f'Iterace {idx+1} - Detekce akcelerací a decelerací')
            ax1.set_xlabel("Čas [s]")
            ax1.set_ylabel("Frekvence [bpm]")
            ax1.legend(loc='upper right')
            ax1.grid(True)

            # Graf 2: Očištěný signál
            ax2 = axs2[i]
            ax2.plot(t, fhr_interp, label='Původní signál', color='gray', alpha=0.6)
            ax2.plot(t, cleaned_signal, label='Signál bez akcelerací/decelerací', color='black')
            ax2.plot(t, baseline, label='Baseline', color='red')

            for j, (start, _) in enumerate(accel_regions):
                ax2.plot(t[start], baseline[start], '^', color='green', label='Akcelerace' if j == 0 else "")
            for j, (start, _) in enumerate(decel_regions):
                ax2.plot(t[start], baseline[start], 'v', color='blue', label='Decelerace' if j == 0 else "")

            ax2.set_title(f'Iterace {idx+1} - Očištěný signál')
            ax2.set_xlabel("Čas [s]")
            ax2.set_ylabel("Frekvence [bpm]")
            ax2.legend(loc='upper right')
            ax2.grid(True)

        plt.tight_layout()

    return cleaned_signal


def vypis_parametrizaci(iterations, fhr_interp, fs):
    print("\n--- Parametrizace iterací ---")
    for i, baseline in enumerate(iterations):
        accel, decel = detect_accel_and_decel(fhr_interp, baseline, fs)
        print(f"Iterace {i+1}:")
        print(f" - Akcelerací: {len(accel)}")
        print(f" - Decelerací: {len(decel)}")
        print(f" - Baseline: min={np.min(baseline):.2f}, max={np.max(baseline):.2f}, mean={np.mean(baseline):.2f}")
        print("")



mat = scipy.io.loadmat(r'data/data_FHR.mat')
fhr = mat['fhr'][:, 0].astype(float)

fhr_nan = fhr.copy()
fhr_nan[fhr_nan == 0] = np.nan

fs = 4  # Hz
t = np.arange(len(fhr_nan)) / fs 

# 1. iterace
fhr_interp = interpolace(fhr_nan,t)

iterations, filtered_signals = baseline(fhr_interp, t, fs)
vypis_parametrizaci(iterations, fhr_interp, fs)


cleaned_signal = plots_akce_deakce(t, fhr, fhr_interp, iterations, filtered_signals, fs)
fhr_nan = cleaned_signal.copy()
fhr_nan[fhr_nan == 0] = np.nan

# 2. iterace
fhr_interp = interpolace(fhr_nan,t)

iterations, filtered_signals = baseline(fhr_interp, t, fs)
vypis_parametrizaci(iterations, fhr_interp, fs)


cleaned_signal = plots_akce_deakce(t, fhr, fhr_interp, iterations, filtered_signals, fs)
fhr_nan = cleaned_signal.copy()
fhr_nan[fhr_nan == 0] = np.nan

# 3. iterace
fhr_interp = interpolace(fhr_nan,t)

iterations, filtered_signals = baseline(fhr_interp, t, fs)
vypis_parametrizaci(iterations, fhr_interp, fs)


cleaned_signal = plots_akce_deakce(t, fhr, fhr_interp, iterations, filtered_signals, fs)

fhr_nan = cleaned_signal.copy()
fhr_nan[fhr_nan == 0] = np.nan
fhr_interp = interpolace(fhr_nan,t)

plt.figure(figsize=(12, 5))
plt.plot(t, fhr_interp, color='black')
plt.title("Finální FHR signál po 3 iteracích čištění")
plt.xlabel("Čas [s]")
plt.ylabel("Frekvence [bpm]")
plt.grid(True)
plt.tight_layout()
plt.show()



plt.show()

