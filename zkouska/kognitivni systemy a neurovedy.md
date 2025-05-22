# Shrnutí ke zkoušce: Klasifikace a shluková analýza

## 🧠 Co je klasifikace?
- Přiřazení objektu do jedné z předem známých tříd
- Objekt reprezentován vektorem příznaků (features)
- Příklady:
  - Předpověď úspěšnosti studentů
  - Diagnostika pacientů na základě symptomů

---

## 🔢 Klasifikace vs. regrese
- **Klasifikace**: výstupem je třída (např. zdravý/nemocný)
- **Regrese**: výstupem je reálné číslo (např. predikce teploty)

---

## ⚙️ Základní klasifikátory

### 📍 K-NN (Nearest Neighbor)
- 1-NN: vezme nejbližší soused
- K-NN: vezme K nejbližších a rozhodne podle většiny
- Výhody: jednoduchost, rychlé učení
- Nevýhody: pomalá predikce, neefektivní u velkého množství příznaků

### 🧠 Bayesovské klasifikátory
- Využívají Bayesovu větu k výpočtu pravděpodobnosti tříd

### 🌲 Rozhodovací stromy
- Indukce stromu → rozhodování → případně prořezání
- Výhody: jednoduchost, pravidla
- Nevýhody: horší pro spojitá data nebo chybějící hodnoty

### 🌳 Random Forest
- Kombinace mnoha rozhodovacích stromů (ensemble learning)

### 💡 SVM (Support Vector Machine)
- Maximální margin mezi třídami, používá support vektory
- Kernelová metoda umožňuje nelineární dělení prostoru

### 🔗 Neuronové sítě
- Složitější modely schopné učení z velkého množství dat

---

## 🧪 Meta klasifikátory
- **Bagging**: bootstrap a kombinace modelů
- **Boosting**: iterativní zlepšování
- **Stacking**: kombinace různých modelů

---

## 🧼 Předzpracování dat

### 🔍 Detekce outlierů
- Hodnoty mimo rozsah → mohou ovlivnit klasifikátor
- Zobrazení: např. boxplot

### 🧮 Normalizace a selekce příznaků
- Výběr nejvhodnějších vlastností (kritéria: přesnost, entropie...)
- Metody: individual ranking, SFS, SBE, evoluční algoritmy

### 📉 Redukce rozměru
- Např. PCA (Principal Component Analysis)

### ⚠️ Nerovnoměrné zastoupení tříd
- Problém: nevyvážený dataset
- Řešení: undersampling, oversampling

---

## 📈 Hodnocení klasifikátoru

### 📊 Metody:
- Accuracy = (TP+TN)/(celkem)
- Sensitivity (Recall) = TP / (TP + FN)
- Specificity = TN / (TN + FP)

### 📉 ROC křivka:
- Zobrazuje vztah mezi senzitivou a specificitou
- AUC = plocha pod ROC křivkou

---

## 🔄 Generalizace a testování

- **Hold-out metoda**: data rozdělena na trénovací/testovací
- **Křížová validace (Cross-validation)**: např. 5-fold
- Cíl: vyhnout se **overfittingu**

---

## 🧬 Shluková analýza (Clustering)
- **Cíl**: najít přirozené skupiny v datech (bez učitele)
- **K-means**: zadáme počet shluků K, algoritmus je najde
- **Hierarchické shlukování**: výstup = dendrogram

---

## 📝 Shrnutí

- Výběr kvalitních příznaků
- Správné dělení dat na trénovací/testovací množinu
- Vhodný klasifikátor a způsob hodnocení (ROC, AUC, senzitivita...)
- Nejprve zkoušet jednoduché modely (K-NN, stromy), později složitější (SVM, ANN)


