# Sensor Guide

| Sensor | Useful measurement | Cannot establish | Notes |
|---|---|---|---|
| RGB camera | Visible appearance | Hidden composition/polymer grade | Stable lighting and local training data |
| IR break-beam | Arrival/timing | Material type | Debounce and calibrate position |
| Inductive proximity | Suitable conductive metal | Exact alloy, battery chemistry, e-waste | Check range and output interface |
| Load cell + HX711 | Mass | Material identity | Static station; tare and known-mass calibration |
| Moisture | Relative/raw response | Material class alone | Calibrate; surface contamination matters |
| Capacitive | Dielectric clue | Definitive material identity | Optional and environment-sensitive |
| RGB colour | Surface colour | Material identity | Stains, labels and lighting affect values |
| ToF/ultrasonic | Distance/fill height | Material type | Calibrate mounting geometry |
| Gate limit switch | End-position feedback | Correct waste category | Useful for actuator diagnostics |
| Motor current | Load/jam clue | Exact jam cause | Establish normal operating baseline |

## Suggested starting set
Begin with camera, arrival photoelectric sensor and inductive sensor. Add a load cell only if a static weigh station is practical. Add moisture only after controlled tests show it improves classification. Include bin-full sensing and gate position feedback in any physical design. Avoid purchasing every optional sensor before the design is evaluated.

## Electrical precautions
- Verify each sensor supply and output voltage against ESP32 limits.
- Use level shifting or opto-isolation for 5/12/24V industrial outputs.
- Condition analog outputs appropriately.
- Never power motors or servos from ESP32 GPIO.
- Use rated motor drivers, fuses, suitable power supplies and proper grounding.
