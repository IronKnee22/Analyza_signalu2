## 📘 Základy EKG

### Co je EKG?
- Elektrokardiogram (EKG) je záznam elektrické aktivity srdce.
- Měří se pomocí elektrod na povrchu těla.
- Výsledkem je graf závislosti elektrického napětí na čase (v mV).

---

## ⚡ Umístění elektrod a svodů

### Končetinové svody
- 3 nebo 4 elektrody na končetinách.
- Historicky: Willem Einthoven (1903), Nobelova cena 1904.

### 12svodové EKG
- 4 končetinové elektrody + 6 elektrod na hrudníku.
- Umožňuje komplexní snímání elektrické aktivity ze srdce.

---

## 📈 Struktura EKG signálu

### Kvaziperiodický signál s opakujícím se srdečním cyklem:
- **P vlna** – depolarizace síní
- **QRS komplex** – depolarizace komor
- **T vlna** – repolarizace komor

### Délky vln a intervalů:
- P vlna: ~80 ms
- PR interval: 120–200 ms
- QRS komplex: 80–100 ms
- T vlna: ~160 ms
- Korigovaný QT interval: < 400 ms
  - QT korigováno dělením odmocninou délky RR intervalu

---

## 🔧 Zpracování signálu

### Odstranění driftu izolinie
- **Příčiny**: dýchání, pohyb, špatný kontakt elektrod
- **Filtry a metody**:
  - Hornopropustní FIR/IIR filtr
  - Spline, klouzavý průměr, mediánový filtr
  - Savitzky-Golay filtr
  - Přehled: [arXiv:1807.11359](https://arxiv.org/abs/1807.11359)

### Odstranění rušení
- **Zdroje rušení**:
  - Elektrická síť: 50 Hz
  - Svalové artefakty: 20–1000 Hz
- **Metody**:
  - Pásmové propusti FIR, IIR
  - Přehled: [IET paper](https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/iet-spr.2020.0104)

---

## 📍 Detekce EKG vln

### Detekce R-vlny
- Nejvýraznější prvek EKG
- **Metoda**: prahování pomocí `findpeaks`
  - `MinPeakDistance = 0.35 s`
  - `MinPeakHeight = 2 mV`

### Detekce dalších vln
- Komplexní úloha, často založená na empirických pravidlech
- Nástroj: [NeuroKit2 – ECG delineace](https://neurokit2.readthedocs.io/en/latest/_modules/neurokit2/ecg/ecg_delineate.html)

---

## 💓 HRV – Heart Rate Variability

### Základní pojmy:
- **NN interval** = RR interval bez artefaktů

### HRV parametry:
- `SDNN`: směrodatná odchylka NN intervalů
- `RMSSD`: odmocnina střední hodnoty druhých mocnin rozdílů NN
- `NN50`: počet po sobě jdoucích NN intervalů lišících se >50 ms
- `pNN50`: poměr NN50 k celkovému počtu NN intervalů

### Využití:
- Marker aktivity autonomního nervového systému
- Užitečné pro analýzu stresu, zátěže, schopnosti rozhodování
- Typická délka analyzovaného okna: 10 s a více

---

## 📚 Databáze

- Fyzikální databáze signálů: [PhysioNet Databáze](https://physionet.org/about/database/)

