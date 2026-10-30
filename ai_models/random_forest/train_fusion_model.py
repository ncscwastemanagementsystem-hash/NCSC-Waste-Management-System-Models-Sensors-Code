"""Train a Random Forest sensor-fusion pipeline. Synthetic CSV is for smoke tests only."""
import argparse
from pathlib import Path
import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

NUMERIC = ["visual_confidence", "metal_detected", "weight_g", "moisture_pct", "capacitive_raw"]
CATEGORICAL = ["visual_class"]
TARGET = "label"

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--csv", required=True)
    p.add_argument("--out", default="models/fusion_model.joblib")
    p.add_argument("--test-size", type=float, default=0.25)
    p.add_argument("--seed", type=int, default=42)
    a = p.parse_args()
    df = pd.read_csv(a.csv)
    required = NUMERIC + CATEGORICAL + [TARGET]
    missing = set(required) - set(df.columns)
    if missing:
        raise SystemExit(f"Missing columns: {sorted(missing)}")
    df = df.dropna(subset=[TARGET])
    X, y = df[NUMERIC + CATEGORICAL], df[TARGET].astype(str)
    if y.nunique() < 2:
        raise SystemExit("At least two target classes are required.")
    counts = y.value_counts()
    stratify = y if counts.min() >= 2 and len(y) * a.test_size >= y.nunique() else None
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=a.test_size,
                                           random_state=a.seed, stratify=stratify)
    prep = ColumnTransformer([
        ("num", Pipeline([("impute", SimpleImputer(strategy="median")),
                          ("scale", StandardScaler())]), NUMERIC),
        ("cat", Pipeline([("impute", SimpleImputer(strategy="most_frequent")),
                          ("onehot", OneHotEncoder(handle_unknown="ignore"))]), CATEGORICAL)
    ])
    pipe = Pipeline([("prep", prep), ("rf", RandomForestClassifier(
        n_estimators=300, class_weight="balanced", min_samples_leaf=2,
        random_state=a.seed, n_jobs=-1))])
    pipe.fit(Xtr, ytr)
    pred = pipe.predict(Xte)
    print("Held-out accuracy (meaningful only with representative real data):", round(accuracy_score(yte, pred), 3))
    print(classification_report(yte, pred, zero_division=0))
    labels = sorted(y.unique())
    print("Confusion matrix labels:", labels)
    print(confusion_matrix(yte, pred, labels=labels))
    out = Path(a.out); out.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump({"pipeline": pipe, "features": NUMERIC + CATEGORICAL,
                 "classes": labels, "warning": "Validate on independent representative real data."}, out)
    print("Saved:", out)

if __name__ == "__main__":
    main()
