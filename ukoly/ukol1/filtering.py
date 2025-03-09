from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import medfilt, iirnotch, filtfilt, firwin, find_peaks
from scipy.fft import rfft, rfftfreq

def median_filter(ecg, fs):
    window_size = fs // 4  # velikost okna je 0.25s 
    if window_size % 2 == 0:
        window_size += 1  

    baseline = medfilt(ecg, kernel_size=window_size)
    return ecg - baseline, baseline
    
def notch_filter(signal, freq, fs, quality_factor=50):
    b, a = iirnotch(freq, quality_factor, fs)
    return filtfilt(b, a, signal)

def fir_bandpass(ecg, lowcut, highcut, fs, num_taps):
    fir_coeff = firwin(num_taps, [lowcut, highcut], pass_zero='bandpass', fs=fs/2)
    return  filtfilt(fir_coeff, [1], ecg) 

def fft(signal, fs):
    fft_values = rfft(signal)  
    freqs = rfftfreq(len(signal), 1/fs)
    fft_values_abs = np.abs(fft_values)
    return fft_values_abs, freqs

mat = loadmat('ecg.mat')
ecg = mat['ecg118e00'][:, 0]  

fs = 250  # vzorkovací frekvence
dt = 1/fs
t = np.arange(0, len(ecg) * dt, dt)

ecg_corrected, baseline = median_filter(ecg, fs)
ecg_notched = notch_filter(ecg_corrected, 50, fs)
ecg_fir_filtered = fir_bandpass(ecg_notched, 0.5, 40, fs, 101)

ecg_fft, ecg_fs= fft(ecg, fs)
ecg_corrected_fft, ecg_fs= fft(ecg_corrected, fs)
ecg_notched_fft, ecg_fs= fft(ecg_notched, fs)
ecg_fir_filtered_fft, ecg_fs= fft(ecg_fir_filtered, fs)

mean_height = np.mean(ecg_fir_filtered)
std_height = np.std(ecg_fir_filtered)
threshold = mean_height + 1.2 * std_height

peaks, _ = find_peaks(ecg_fir_filtered, distance=fs//2.5, height=threshold)

plt.figure(figsize=(12, 12))

plt.subplot(4, 2, 1)
plt.plot(t, ecg, label="Původní EKG", alpha=0.7)
plt.plot(t, baseline, label="Izolinie",ls='--', color='red')
plt.xlabel("Čas (s)")
plt.ylabel("Amplituda")
plt.title("Původní EKG signál")
plt.legend()

plt.subplot(4, 2, 3)
plt.plot(t, ecg_corrected, label="Po mediánovém filtru", color="green")
plt.xlabel("Čas (s)")
plt.ylabel("Amplituda")
plt.title("EKG po odstranění driftu izolinie")
plt.legend()

plt.subplot(4, 2, 5)
plt.plot(t, ecg_notched, label="Po Notch filtru (50 Hz)", color="orange")
plt.xlabel("Čas (s)")
plt.ylabel("Amplituda")
plt.title("EKG po odstranění rušení 50 Hz")
plt.legend()

plt.subplot(4, 2, 7)
plt.plot(t, ecg_fir_filtered, label="Po FIR pásmové propusti (0.5-40 Hz)", color="blue")
plt.xlabel("Čas (s)")
plt.ylabel("Amplituda")
plt.title("EKG po FIR pásmové propusti")
plt.legend()

plt.subplot(4, 2, 2)
plt.plot(ecg_fs, ecg_fft, label="FFT Původního EKG")
plt.xlabel("Frekvence (Hz)")
plt.ylabel("Amplituda")
plt.title("Spektrum původního signálu")
plt.legend()

plt.subplot(4, 2, 4)
plt.plot(ecg_fs, ecg_corrected_fft, label="FFT po mediánovém filtru", color="green")
plt.xlabel("Frekvence (Hz)")
plt.ylabel("Amplituda")
plt.title("Spektrum signálu po odstranění driftu izolinie")
plt.legend()

plt.subplot(4, 2, 6)
plt.plot(ecg_fs, ecg_notched_fft, label="FFT po Notch filtru", color="orange")
plt.xlabel("Frekvence (Hz)")
plt.ylabel("Amplituda")
plt.title("Spektrum signálu po odstranění 50 Hz rušení")
plt.legend()

plt.subplot(4, 2, 8)
plt.plot(ecg_fs, ecg_fir_filtered_fft, label="FFT po FIR filtru", color="blue")
plt.xlabel("Frekvence (Hz)")
plt.ylabel("Amplituda")
plt.title("Spektrum signálu po pásmové propusti 0.5-40 Hz")
plt.legend()

plt.tight_layout()

plt.figure(figsize=(12, 10))
plt.plot(t, ecg_fir_filtered, label="Původní EKG", alpha=0.7, color='green')
plt.scatter(t[peaks], ecg_fir_filtered[peaks], color="red", label="R-vlny", zorder=3)

plt.xlabel("Čas (s)")
plt.ylabel("Amplituda")
plt.title("Původní EKG signál")
plt.legend()


plt.show()

