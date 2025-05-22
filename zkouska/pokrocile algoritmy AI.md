# 🧠 1. Rozdělení AI

- **Machine Learning (ML)**: Supervised, Unsupervised, Semi-supervised, Reinforcement Learning  
- **Neural Networks (NN)**: CNN, RNN, LSTM, Autoencoder  
- **Deep Learning**: Hierarchické vrstvy NN  
- **Evoluční algoritmy**: Genetické algoritmy  
- **Zpracování přirozeného jazyka (NLP)**: LLM, Transformers, Autoregressive models  
- **Další oblasti**: Počítačové vidění, Robotika  

---

## 🤖 2. Machine Learning (Strojové učení)

### Typy ML:
- **Supervised**: Trénink na označených datech (např. SVM, Random Forest)  
- **Unsupervised**: Neoznačená data, hledání struktur (PCA, SVD, K-means)  
- **Semi-supervised**: Kombinace označených a neoznačených dat  
- **Reinforcement Learning**: Učení z odměn a interakcí s prostředím  

### Aplikace:
- Diagnostika nemocí, predikce léčby, personalizovaná medicína  
- Segmentace obrazů, klasifikace genomických dat  
- Automatická anotace, klasifikace proteinů, EHR analýza  

### Algoritmy:
- **Lineární regrese**: Predikce (např. krevní tlak, růst)  
- **Logistická regrese**: Predikce nemocí  
- **K-nn**: Detekce diabetu, klasifikace nemocí  
- **SVM**: Rozpoznávání patologií (epilepsie, arytmie)  

---

## 🧠 3. Deep Learning (Hloubkové učení)

### CNN (Konvoluční neuronové sítě):
- Extrakce příznaků z obrázků  
- Vrstva konvoluce, pooling, fully-connected, softmax  
- Aplikace: rozpoznání obrazů, klasifikace  

### GANs (Generativní adversariální sítě):
- **Generátor** + **Diskriminátor**  
- Generování realistických dat, super-resolution, odstranění šumu  
- Využití: trénovací data, rekonstrukce a doplňování snímků  

### Autoenkodéry:
- Neřízené učení, redukce dimenze, odstranění šumu  
- **Enkodér** → latentní prostor → **Dekodér**  
- Ztrátová funkce: MSE  
- Využití: vizualizace, anomaly detection, segmentace  

---

## 🔁 4. Transformerové sítě

- Základ pro moderní NLP (např. BERT, GPT)  
- **Attention Mechanism**, **Self-Attention**  
- **Positional Encoding**, **Feed-forward NN**, **Residual connections**  
- **Encoder–Decoder architektura**  

### Aplikace:
- BERT: klasifikace, otázky/odpovědi, NER  
- GPT: generování textu, překlady, shrnutí  

---

## 🧾 5. Genetické algoritmy

- Evoluční optimalizace inspirovaná přírodou  
- **Proces**: Inicializace, fitness, selekce, křížení, mutace  

### Výhody:
- Řešení složitých problémů, flexibilita  

### Nevýhody:
- Výpočetně náročné, závislost na parametrech  

---

## 🧪 6. Příklady použití AI v neurologii

- **Alzheimer** – klasifikace MR pomocí SVM (96 % přesnost)  
- **Epilepsie** – predikce záchvatů pomocí LSTM  
- **Leukoaraióza** – detekce lézí z CT pomocí Random Forest  
- **DeepNAT** – segmentace mozku pomocí CNN  
- **EEG analýza** – genetické algoritmy pro optimalizaci NN  

---

## 🏥 7. AI v české medicíně

- Aireen, Neurona Lab, Kardi AI, MAIA Labs, Carebot  

### Výhody AI v medicíně:
- Analýza velkých datasetů  
- Rychlá a přesná diagnostika  
- Automatická anotace, upozornění, personalizace léčby  
- Efektivita, dostupnost 24/7, telemedicína  

### Výzvy:
- Data a soukromí, etika, spolehlivost  
- Integrace do klinické praxe, regulace, standardizace  

---

## 🧮 8. Stavba neuronových sítí (Python)

- Klasifikace do 2 tříd  
- Skrytá vrstva s nelineární aktivací  
- Chybová funkce: cross-entropy  
- Forward & Back propagation  
- Knihovny: numpy, sklearn, matplotlib  
