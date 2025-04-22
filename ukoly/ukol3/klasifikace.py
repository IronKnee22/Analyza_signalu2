import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

dfs = [pd.read_csv(f"data/features/features_subject_{i}.csv") for i in range(1, 10)]
df_combined = pd.concat(dfs, ignore_index=True)

X = df_combined.drop("Class", axis=1)
y = df_combined["Class"]
X_test_final = pd.read_csv("data/features/features_subject_10.csv")

classifiers = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "SVM": SVC(kernel="rbf", C=1.0, gamma="scale", random_state=42),
}

best_model = None
best_score = 0
best_name = ""

for name, model in classifiers.items():
    scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")
    mean_score = np.mean(scores)
    print(f"{name} accuracy (5-fold CV): {mean_score:.4f}")

    if mean_score > best_score:
        best_score = mean_score
        best_model = model
        best_name = name

print(f"\n✅ Nejlepší model: {best_name} (accuracy: {best_score:.4f})")

best_model.fit(X, y)
predicted_classes = best_model.predict(X_test_final)

output_filename = (
    f"data/results/marek_darsa_pokus1_{best_name.lower().replace(' ', '')}.csv"
)
np.savetxt(output_filename, predicted_classes, fmt="%d")
print(f"Výsledky uloženy do {output_filename}")
