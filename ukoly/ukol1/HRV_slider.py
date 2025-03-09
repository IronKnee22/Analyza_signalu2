import tkinter as tk
from tkinter import ttk
from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import medfilt, iirnotch, filtfilt, firwin, find_peaks
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

def calculate_hrv(rr_intervals):
    if len(rr_intervals) < 2:
        return [0, 0, 0, 0, 0]

    hr = 60000 / np.mean(rr_intervals) # rr je v milisekundách takže to musím na to převést taky
    sdnn = np.std(rr_intervals)
    diff_rr = np.diff(rr_intervals)
    rmssd = np.sqrt(np.mean(diff_rr ** 2))
    nn50 = np.sum(np.abs(diff_rr) > 50)
    pnn50 = (nn50 / len(diff_rr)) * 100

    return [round(hr, 2), round(sdnn, 2), round(rmssd, 2), nn50, round(pnn50, 2)]

mat = loadmat('ecg.mat')
ecg = mat['ecg118e00'][:, 0]  

fs = 250  # vzorkovací frekvence
dt = 1/fs
t = np.arange(0, len(ecg) * dt, dt)

ecg_corrected, baseline = median_filter(ecg, fs)
ecg_notched = notch_filter(ecg_corrected, 50, fs)
ecg_fir_filtered = fir_bandpass(ecg_notched, 0.5, 40, fs, 101)

mean_height = np.mean(ecg_fir_filtered)
std_height = np.std(ecg_fir_filtered)
threshold = mean_height + 1.2 * std_height

peaks, _ = find_peaks(ecg_fir_filtered, distance=fs//2.5, height=threshold)

class ECGViewer(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("EKG Viewer")
        self.geometry("1000x800")

        self.scrollbar = ttk.Scale(self, from_=0, to=len(t) - 60 * fs, orient=tk.HORIZONTAL, length=800, command=self.update_plot)
        self.scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.fig, self.ax = plt.subplots(figsize=(10, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.hrv_frame = ttk.LabelFrame(self, text="HRV Parametry (po 10 sekundách)", padding=(10, 5))
        self.hrv_frame.pack(fill=tk.X, padx=10, pady=5)

        self.hrv_labels = []
        for i in range(6):
            label = ttk.Label(self.hrv_frame, text=f"Úsek {i+1}: HR: 0, SDNN: 0, RMSSD: 0, NN50: 0, pNN50: 0", font=("Arial", 10))
            label.pack(anchor="w")
            self.hrv_labels.append(label)

        self.update_plot(0)

    def update_plot(self, val):
        start_idx = int(self.scrollbar.get())  
        end_idx = start_idx + 60 * fs  
        
        if end_idx > len(t):
            end_idx = len(t)
            start_idx = end_idx - 60 * fs
        
        self.ax.clear()
        self.ax.plot(t[start_idx:end_idx], ecg_fir_filtered[start_idx:end_idx], label="Filtrovaný EKG", color='green')

        peaks_in_window = [p for p in peaks if start_idx <= p < end_idx]
        self.ax.scatter(t[peaks_in_window], ecg_fir_filtered[peaks_in_window], color="red", label="R-vlny", zorder=3)

        self.ax.set_xlabel("Čas (s)")
        self.ax.set_ylabel("Amplituda")
        self.ax.set_title("EKG signál s možností posouvání")
        self.ax.legend()
        
        self.canvas.draw()

        hrv_results = self.calculate_hrv_for_visible_window(start_idx, end_idx)
        for i in range(len(hrv_results)):
            self.hrv_labels[i].config(text=f"Blok {i+1}: HR: {hrv_results[i][0]}, SDNN: {hrv_results[i][1]}, RMSSD: {hrv_results[i][2]}, NN50: {hrv_results[i][3]}, pNN50: {hrv_results[i][4]}")

    def calculate_hrv_for_visible_window(self, start_idx, end_idx):
        segment_size = 10 * fs
        hrv_results = []

        for segment_start in range(start_idx, end_idx, segment_size):
            segment_end = segment_start + segment_size
            segment_peaks = [p for p in peaks if segment_start <= p < segment_end]

            if len(segment_peaks) > 1:
                rr_intervals = np.diff([t[p] * 1000 for p in segment_peaks])  # převedeno na ms
                hrv_values = calculate_hrv(rr_intervals)
            else:
                hrv_values = [0, 0, 0, 0, 0]

            hrv_results.append(hrv_values)

        while len(hrv_results) < 6:
            hrv_results.append([0, 0, 0, 0, 0])

        return hrv_results

if __name__ == "__main__":
    app = ECGViewer()
    app.mainloop()
