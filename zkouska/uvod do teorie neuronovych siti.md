## 🧠 Co je to umělá inteligence (AI)?

**Definice dle EU AI Act:**  
Systém fungující autonomně, na základě dat a vstupů dosahuje cíle prostřednictvím strojového učení, logiky a znalostí. Výstupy: obsah, předpovědi, rozhodnutí, doporučení.

---

## 📜 Historie AI (vybrané milníky)

- 1943: První matematický model neuronu
- 1955: Termín AI (John McCarthy)
- 1966: Chatbot ELIZA, robot Shakey
- 1989: Samořídící auto – Testlab 1
- 1996: Deep Blue poráží Kasparova
- 2011: Watson vyhrává Riskuj!
- 2017: AlphaGo porazí Lee Sedola
- 2020: GPT-3 píše knihu

---

## 🧩 Neuronová síť (NN)

- Inspirovaná strukturou a činností biologických neuronů
- Skládá se z mnoha jednoduchých prvků (neuronů)
- Schopnost: učit se, generalizovat, řešit nelineární problémy
- Aplikace: klasifikace, regrese, shlukování, komprese, predikce

---

## 🔬 Stavba neuronu (perceptron)

- **Vstup (input)** – reálná čísla (např. velikost, barva)
- **Váhy (weights)** – důležitost vstupů
- **Bias (práhová hodnota)** – upravuje rozhodovací hranici
- **Aktivační funkce** – např. sigmoid, ReLU, skoková
- **Výstup (output)** – klasifikace, shluk

---

## 🔁 Aktivační funkce (α)

- **Skoková (step)**  
- **ReLU (rectified linear unit)**  
- **Sigmoidální**  
- **Tan-Sigmoid**

---

## 🔠 Typy neuronových sítí

### Podle vrstev:
- Jednovrstvé (Hopfieldova síť)
- Vícevrstvé (MLP, CNN)

### Podle toku dat:
- Feedforward (dopředné)
- Recurrent (rekurentní, se zpětnou vazbou)

### Podle učení:
- Supervised (s učitelem)
- Unsupervised (bez učitele)

### Styl učení:
- Deterministické (backpropagation)
- Stochastické (náhodné váhy)

---

## 📚 Specifické typy NN

### Hopfieldova síť
- Jednovrstvá, rekurentní
- Asociativní paměť, optimalizace

### Kohonenova síť (SOM)
- Učení bez učitele
- Shluková analýza (clustering)
- Mřížka neuronů

### MLP (Multi Layer Perceptron)
- Nejčastější typ NN
- Vrstvy: vstupní – skrytá – výstupní
- Použití: klasifikace, predikce

### CNN (Convolutional Neural Network)
- Pro zpracování obrazu
- Vrstva: konvoluční → pooling → plně propojená

---

## ⚙️ Jak neuronová síť funguje?

1. Inicializace vah a biasu  
2. Definice aktivační funkce (ReLU, sigmoid)  
3. Definice chybové funkce (MSE, cross-entropy)  
4. **Forward propagation**  
5. Výpočet chyby  
6. **Backpropagation** – úprava vah  
7. Iterace

---

## 📉 Chybové funkce

- **MSE (Mean Squared Error)** – regrese  
- **CE (Cross-Entropy)** – klasifikace

---

## 🧪 Problémy neuronových sítí

- Nedostatek dat  
- Špatně označená data  
- **Overfitting** – přeučení  
- **Underfitting** – nenaučení  
- Pomalé učení

---

## 🛠️ Regularizace a prevence overfittingu

- Vhodný počet skrytých vrstev a neuronů  
- Rozšiřování dat (augmentace): otáčení, ořez, šum  
- Normalizace dat  
- **L2 regularizace**  
- **Learning rate** – míra učení  
- **Early stopping**  
- **Dropout** – náhodné vypínání neuronů

---

## 🧪 Vyhodnocení neuronové sítě

- **Recall (Senzitivita)**  
- **Specificita**  
- **F1 skóre**  
- **Precision (PPV)**


