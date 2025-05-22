# Shrnutí ke zkoušce: Geneze, význam a zpracování KTG

## 🩺 Fyziologie plodu a hypoxie

- Srdce plodu začíná bít kolem 4. týdne (65 BPM), frekvence roste s vývojem.
- Placenta zajišťuje výměnu O₂ a CO₂, ale její autonomní funkce není plně známa.
- **Hypoxie – 3 stupně**:
  - **Hypoxemie**: efektivní využívání O₂, omezení pohybu, růstová retardace.
  - **Hypoxie**: centralizace oběhu, aktivace sympatiku, bezpečí centrálních orgánů.
  - **Asfyxie**: kritická fáze, hrozí selhání, nutný urgentní zásah (např. císařský řez).

---

## 📊 Kardiotokogram (KTG)

- Záznam **fetální srdeční frekvence (FHR)** a **děložních kontrakcí (TOCO)**.
- Reaguje na chování plodu, hypoxii a stres.
- Měření:
  - **Externí**: ultrazvuk
  - **Interní**: skalpová elektroda
  - **Abdominální**: elektrody na břiše matky – směs signálů (mateřské/fetální EKG + kontrakce)

---

## 🩺 Klinické hodnocení KTG

- Hodnocení do kategorií: **normální**, **suspektní**, **patologický**
- Velká variabilita mezi lékaři (inter-observer ~70 %, intra-observer ~80 %)
- Vysoká subjektivita, závislost na zkušenostech a případech
- Rizika: zanedbání péče, neopodstatněné císařské řezy

---

## 📏 Hodnocení podle FIGO (1986)

- Definice akcelerací a decelerací
- Hodnocení baseline pomocí histogramu
- Doplněno novějšími metodami automatické analýzy

---

## 🤖 Automatické hodnocení KTG

- **Cíl**: odhalit riziko acidózy, snížit chyby a zbytečné zákroky
- Počítačová analýza = doplněk k lidskému hodnocení

---

## 🧪 CTU-UHB databáze (Brno)

- První veřejná KTG databáze
- Pouze donošené plody (>34. týden)
- 508 normálních (pH > 7.05), 44 patologických (pH ≤ 7.05)

---

## 🧪 Databáze Lyon, FR

- 1251 normálních, 37 patologických
- Vysoká kvalita a rozsah klinických dat

---

## ⚙️ Předzpracování signálu

- **Převzorkování**: z neekvidistantního na ekvidistantní signál
- **RR intervaly**: Tk = tk - tk-1
- **Interpolace** chybějících dat (spline, t < 5s)
- **Artefakty**: až 20 %, časté ke konci porodu

---

## 📐 Klinické a morfologické příznaky

- **Baseline (bazální FHR)** – detekce filtrací nebo histogramem
- **Akcelerace a decelerace**
- Plovoucí baseline: B(t) ≈ β₀ + β₁t
- MADdtrd = mediánová absolutní odchylka od baseline

---

## 📊 Další příznaky

### Lineární:
- Průměr, směrodatná odchylka, šikmost, špičatost
- Variabilita (krátko-/dlouhodobá)
- Spektrální analýza
- Hurstův parametr

### Nelineární:
- Entropie
- Scattering transform
- Multifraktální analýza (MF)
- p-leaders
- Cílem je zachytit nové rysy FHR

---

## 📉 Analýza příznaků

- Výpočet z posledních 20 min. před porodem
- Statistické testy, ROC analýza, cut-off hodnoty
- Dobré výsledky pro: MADdtrd, H, β₀
- Kombinace ve strojovém učení (např. SVM)

---

## 🤖 SVM a Sparse-SVM

- **SVM**: silný klasifikační algoritmus, řídkost dat (sparsity)
- **Sparse-SVM**: zaměřeno na řídkost ve **vlastnostech**, ne v datech
- Zlepšení interpretace a výkonu

---

## 📈 Klasifikace

- Z posledních 20 min. signálu
- Optimální regularizace: C = 2–8.5
- Výsledky: SE = 0.73, SP = 0.75
- Příznaky: MADdtrd, H, β₀

---

## 🔁 Trajektorie v příznakovém prostoru

- Sledování vývoje v čase pomocí 20min oken s 5min překryvem
- d(tk) = y(wᵀx(tk) + b): značí přechod mezi normální a patologickou oblastí

---

## ✅ Shrnutí

- Komplexní metodologie:
  - Získání a příprava dat (CTU-UHB, Lyon)
  - Extrakce a analýza příznaků
  - Klasifikace pomocí SVM
  - Vyhodnocení (senzitivita, specificita)
- **Cíl**: snížit subjektivitu hodnocení KTG a riziko zanedbání péče

