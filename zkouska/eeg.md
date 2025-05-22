# 🧠 Centrální nervový systém (CNS)

- Zahrnuje mozek a páteřní míchu  
- Funkce: vnímání, myšlení, paměť, motorika, řeč  
- Šedá hmota = těla neuronů, dendrity  
- Bílá hmota = axony (nervová vlákna)

---

# 🧠 Mozek – základní přehled

- Hmotnost: cca 1300–1400 g  
- Objem: cca 1450 cm³  
- Spotřeba energie: cca 20 %  

## Stavba:

- **Přední mozek (Prosencephalon)**: thalamus, hypothalamus, hemisféry  
- **Střední mozek (Mesencephalon)**: reflexy, dopamin, bdění/spánek  
- **Zadní mozek (Rhombencephalon)**: mozeček, varolův most, prodloužená mícha

---

# 🧬 Neuron a přenos signálu

- Neuron: základní jednotka CNS  
  - Soma (tělo), dendrity (příjem), axon (výstup)  
  - Myelinová pochva zrychluje přenos  
- Signály se šíří pomocí **akčního potenciálu**  
  - Klidový potenciál: ~ -90 mV  
  - Fáze: depolarizace → repolarizace → hyperpolarizace

---

# 🧬 Klíčové typy mozkové aktivity (vlny)

| Typ vlny | Frekvence | Stav |
|----------|-----------|------|
| Delta    | 0.5–4 Hz  | hluboký spánek |
| Theta    | 4–8 Hz    | ospalost, meditace |
| Alfa     | 8–13 Hz   | relaxace, zavřené oči |
| Beta     | 13–22 Hz  | stres, úzkost |
| Gama     | 22–30 Hz  | soustředění, pozornost |

---

# 💤 Spánek a mozek

- Nedostatek: zhoršené učení, paměť, pozornost, deprese

---

# 🧪 Patologie CNS

- Epilepsie, Alzheimer, Parkinson  
- Mrtvice, deprese, nádory  
- Roztroušená skleróza  

---

# 🖥️ Neurozobrazovací metody

## Strukturální a funkční:

- **CT**: RTG, zobrazení struktur, rychlé, ale ionizující záření  
- **MRI**: magnetická rezonance, detailní, ale drahá  
- **fMRI**: mozková aktivita, měří průtok krve  
- **PET**: metabolická aktivita, Alzheimer, epilepsie  
- **SPECT**: průtok krve, demence, epilepsie  
- **DOT**: optická tomografie (nízké prostorové, vysoké časové rozlišení)  
- **MEG**: měří magnetická pole mozku, lepší prostorové rozlišení než EEG  
- **EEG**: elektrická aktivita mozku (viz níže)

---

# 🔌 EEG – elektroencefalografie

- Měření elektrické aktivity mozku pomocí elektrod  
- Neinvazivní / invazivní (ECoG, SEEG)  
- Standard: **mezinárodní 10-20 systém**  
- Zapojení: unipolární / bipolární  

## Evokované potenciály:

- Zrakové, sluchové, somatosenzorické, motorické  

---

# ⚠️ EEG artefakty

| Typ | Popis |
|-----|-------|
| **Muskulární** | vysokofrekvenční šum (beta/gama) |
| **Pohybové** | pomalé vlny v pásmu delta/theta |
| **Okulární** | mrkání – silný signál ve frontálních elektrodách |
| **Kardiální** | rytmický šum odpovídající EKG |
| **Síťový brum** | šum na 50/60 Hz (síťové rušení) |
| **Špatná reference** | náhlé změny ve všech kanálech |

---

# 🧹 Odstraňování artefaktů

- **Manuální kontrola**  
- **Filtrování**  
- **ICA (Independent Component Analysis)**  
- **PCA (Principal Component Analysis)** – redukce dimenze, extrakce vlastností  

---

# 📉 Entropie v EEG

- Měření složitosti signálu, diagnostika stavů mozku  

| Typ entropie | Popis a využití |
|--------------|-----------------|
| **Spektrální** | rozložení energie, stav vědomí |
| **Permutační** | sledování predikovatelnosti signálu |
| **SampEn/ApEn** | měření nepravidelnosti signálu |
| **Shannonova** | klasická informační entropie |

---

# 📊 Využití EEG

- Krátkodobá i dlouhodobá vyšetření (epilepsie, spánek, poranění, demence)  
- Výzkum, biofeedback terapie  

---

# 🧩 Rozšířené metody zpracování EEG signálu

## 🧹 Detekce artefaktů

- **Pohybové artefakty**: automatická detekce pomocí histogramu  
- **Mrkání**: kombinace různých prahování (na základě šumu, vrcholů, výsledný práh)  
- **Zobrazování průběhu detekce** – syrový signál, filtrovaný signál, detekované špičky  

---

## ✂️ Segmentace EEG signálu

### Typy segmentace:

- **Konstantní** (např. 0.1 s, 0.5 s, 1 s, 5 s, 10 s)  
- **Adaptivní segmentace** s parametry:  
  - `window_size`, `window_shift`  
  - `segment_length_min`, `segment_length_max`  
  - `envelope_filtrconst`, `envelope_hysteresis`  

### Účel:

- Rozdělit nestacionární EEG na stacionární úseky vhodné pro zpracování  

---

## 📊 Extrakce a selekce příznaků

- **Multikanálová analýza** (EEG, EMG, EOG, EKG)  
- Příznaky:  
  - **PSD** (Power Spectral Density)  
  - **Autokorelace**  
  - **STD EMG** – detekce pohybu  
  - **EOG – FIR-mediánový hybridní filtr**  
- **Selekce příznaků** – výběr nejrelevantnějších atributů  

---

## 🧠 Klasifikace EEG

### Postup:

1. Segmentace signálu  
2. Výpočet příznaků  
3. Vytvoření trénovací množiny (např. normální vs. epileptické EEG)  
4. Klasifikace každého segmentu  

### Aplikace:

- Klasifikace spánku: Wake, REM, NREM1–4  
- Klasifikace kómatu  
- Novorozenecké EEG – zralost mozku  

---

## 🌐 Shluková analýza EEG

- **Hierarchické shlukování** – dendrogramy  
- **K-means** – clustering segmentů podle příznaků  
- Ukázky: epileptická EEG, komatózní EEG, spánková PSG data  

---

## 🎨 Vizualizace a transformace

- **2D/3D spektrogramy** – čas-frekvenční vývoj EEG  
- **2D a 3D mapování hlavy** – např. rozložení výkonu ve frekvenčním pásmu  
- **Spektrogram spánkového EEG** – detekce periodických struktur  

---

## 📡 EEG Koherence

- Měří synchronizaci mezi oblastmi mozku  
- Využití: biofeedback, kognitivní výzkum  

---

## 🔁 Inverzní problém EEG

- **Dopředný problém**: z 3D dipólů spočítat 2D EEG  
- **Inverzní problém**: z 2D EEG odvodit 3D dipóly → **neexistuje jednoznačné řešení**  

---

## ⚙️ Matlabové nástroje a knihovny

- **EEGLAB** – open-source toolbox pro EEG/MEG analýzu  
- Klíčové funkce:  
  - `buffer()` – segmentace signálu  
  - `bandpower()` – výkon v pásmu (např. [4 8] Hz)  
  - `wentropy()` – Shannonova entropie  
  - `kmeans()`, `linkage()` – shlukování  
  - `spectrogram()` + `imagesc()` – vizualizace  

---

## 🧪 Další příznaky

- Základní: `min`, `max`, `mean`, `std`  
- Tvar: `skewness`, `kurtosis`  
- Složitější:  
  - Shannonova entropie  
  - Fraktální dimenze  
  - Koeficienty waveletů  
  - Koherence, korelace, autokorelace  
