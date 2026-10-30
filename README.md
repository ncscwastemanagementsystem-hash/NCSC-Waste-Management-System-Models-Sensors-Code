# NCSC Smart Waste-to-Resource System — Models, Sensors & Code

Research-stage starter repository for the NCSC Smart Waste-to-Resource System. This repository contains proposed architecture, AI starter scripts, sensor examples, ESP32 demonstrations, documentation and tests. It does not claim that a physical sorter has been built or validated.

## Proposed workflow
Hopper → vibrating spreader → conveyor → IR/photoelectric arrival trigger → camera + YOLO detection → supporting sensor readings → Random Forest sensor fusion → conservative safety decision → supervised diverter → category bins and bin-level monitoring.

An IR/photoelectric sensor detects presence and timing, not material identity. A vibrating tray spreads objects but does not guarantee one-at-a-time feeding. Camera, moisture, colour, inductive and capacitive readings all have limitations.

## Categories
organic, plastic, paper_cardboard, glass, e_waste, metal, other_residual, manual_inspection and reject. Batteries, aerosols, sharps, medical waste, unknown chemicals and hazardous items must be isolated for trained/manual handling and authorised disposal.

## Structure
- `ai_models/`: YOLO inference and Random Forest sensor-fusion training
- `sensors/`: ESP32 examples for IR, inductive, load cell, moisture and bin-level sensors
- `firmware/`: supervised ESP32 diverter demonstration
- `software/`: decision policy and serial bridge
- `sample_data/`: synthetic demonstration data only
- `docs/`: architecture, installation, sensors, safety and validation
- `tests/`: basic policy tests

## Python setup
Use Python 3.10 or 3.11:
```bash
python -m venv .venv
source .venv/bin/activate
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
python ai_models/random_forest/train_fusion_model.py --csv sample_data/synthetic_sensor_dataset.csv
pytest -q
```
The bundled CSV is synthetic and cannot establish real-world model accuracy.

## YOLO camera
```bash
pip install -r requirements-yolo.txt
python ai_models/yolo/detect_camera.py --weights path/to/your/best.pt --source 0
```
Provide your own trained waste-detection weights and validate them on an independent representative dataset.

## Hardware safety
Verify sensor voltages before connecting to ESP32 pins. Use level shifting/isolation for higher-voltage outputs. Never drive motors or servos directly from GPIO. Use rated drivers, guarded mechanisms, gate feedback and a physical emergency-stop circuit. A single servo flap cannot route eight categories. The firmware examples are bench demonstrations, not certified safety controls.

## Validation
Report per-class precision, recall, F1, confusion matrix, reject rate and physical routing success separately. An 80% accuracy value is only a proposed target, not an achieved result. Start in supervised/manual mode; send uncertain or conflicting readings to manual inspection.
