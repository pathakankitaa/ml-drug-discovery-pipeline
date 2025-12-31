import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

# Example dataset
data = pd.read_csv("data/ligands.csv")

X = data.drop("label", axis=1)
y = data["label"]

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

scores = cross_val_score(model, X, y, cv=5, scoring="roc_auc")
print("Mean ROC-AUC:", scores.mean())
