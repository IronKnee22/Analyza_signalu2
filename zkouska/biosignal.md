## 🧠 1. Základy biosignálů

### Co je signál?
- Mění se v čase, přenáší informaci.
- Matematicky popsatelný (např. amplituda, frekvence).

### Co je biosignál?
- Specifický signál měřený na živém organismu.
- Měří se elektrické, magnetické, mechanické, chemické nebo akustické projevy organismu.
- Využití: diagnostika, monitorování, výzkum.

---

## 📊 2. Typy biosignálů

### A) Jednorozměrné biosignály

#### Bioelektrické signály

| Název       | Amplituda (mV) | Frekvence (Hz) | Popis                                         |
|-------------|----------------|----------------|-----------------------------------------------|
| EKG         | 0.5–4          | 0.5–125(150)   | Snímaní el. aktivity srdce z povrchu těla     |
| fEKG        | 0.01–0.1       | 0.01–150       | Aktivita srdce plodu (přes břicho matky)      |
| EEG         | 0.001–0.3      | 0.1–80         | Aktivita mozku z povrchu hlavy                |
| ECoG        | 0.01–1         | 0.1–100        | Aktivita mozku z přímého kontaktu s mozkem    |
| EMG         | 0.1–5          | 0–10000        | Aktivita svalů, snímaná povrchově nebo vpichy |
| EOG         | 0.01–3(5)      | 0.05–100       | Aktivita sítnice okolo očí                    |
| EGG         | 0.01–1         | 0.01–1         | Aktivita žaludku (z břicha)                   |

#### Biomagnetické signály

| Název       | Amplituda (pT) | Frekvence (Hz) | Popis                            |
|-------------|----------------|----------------|----------------------------------|
| MKG         | 50–70          | 0.5–150        | Magnetická aktivita srdce        |
| fMKG        | 1              | 0.05–100       | Magnetická aktivita srdce plodu  |
| MEG         | 1–2            | 0.5–30         | Magnetická aktivita mozku        |
| MMG         | 10–90          | 0–20000        | Magnetická aktivita svalů        |
| MOG         | 10             | 0.1–100        | Magnetická aktivita očí          |

---

### B) Více-/dvourozměrné signály

- **UZ (Ultrazvuk)**: Akustické vlnění > 20 kHz, diagnostika měkkých tkání, bezpečný.
- **RTG**: Elektromagnetické záření, diagnostika kostí, škodlivé.
- **CT**: Počítačová tomografie (rotující rentgenka, 3D obraz).
- **MRI**: Magnetická rezonance (voda v tkáních, kontraindikace: implantáty, tetování).
- **PET**: Funkční vyšetření pomocí radiofarmak, často kombinováno s CT.

---

## 🧰 3. Snímací řetězec

### Snímání
- Elektrody Ag-AgCl s gelem.
- Galvanické oddělení (optický člen: LED + fototranzistor).

### Zesilování signálu
- Vstupní odpor: 1–10 MΩ
- Zesílení: 60–100 dB
- CMRR ≥ 100 dB (potlačení rušení)

---

## 💾 4. Digitalizace signálu

### Vzorkování
- Frekvence: 125–2000 Hz
- Podmínka Shannonova teorému: `f_vz ≥ 2 * f_max`

### Kvantování
- Rozlišení: 12–16 bit
- Kvantizační chyba: ± q/2
- `SNR = 20 log (2^n)`

---

## 🧮 5. Zpracování signálu

### Časově-frekvenční analýza
- Fourierova transformace
- STFT
- Vlnková transformace

### Filtrace
- Horní / dolní propust
- Adaptivní filtry

---

## 📐 6. Popis signálu a příznaky

### Atributy (features)
- Amplitudy, intervaly, statistické parametry
- Transformace: PCA, ICA

### EKG příznaky
- Intervaly: P-P, R-R, Q-T, P-Q, S-T, QRS
- Amplitudy: P, Q, R, S, T, U

---

## 🤖 7. Zpracování a nástroje

### Formáty
- EDF(+), MIT/WFDB, AHA

### Databáze
- PhysioNet, biosignal.at

### Nástroje
- BioSig (Matlab, Octave, C++)
- SigViewer (Qt GUI)


