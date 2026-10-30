"""Predict one item from structured sensor readings."""
import argparse
import joblib
import pandas as pd

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--model", default="models/fusion_model.joblib")
    p.add_argument("--visual-class", required=True)
    p.add_argument("--visual-confidence", type=float, required=True)
    p.add_argument("--metal-detected", type=int, choices=[0, 1], required=True)
    p.add_argument("--weight-g", type=float, required=True)
    p.add_argument("--moisture-pct", type=float, required=True)
    p.add_argument("--capacitive-raw", type=float, default=0)
    a = p.parse_args()
    bundle = joblib.load(a.model)
    row = pd.DataFrame([{"visual_class": a.visual_class,
        "visual_confidence": a.visual_confidence, "metal_detected": a.metal_detected,
        "weight_g": a.weight_g, "moisture_pct": a.moisture_pct,
        "capacitive_raw": a.capacitive_raw}])
    model = bundle["pipeline"]
    label = model.predict(row)[0]
    probability = float(max(model.predict_proba(row)[0]))
    print({"predicted_label": str(label), "model_probability": round(probability, 4),
           "warning": "Probability is not a safety guarantee; apply manual inspection policy."})

if __name__ == "__main__":
    main()
