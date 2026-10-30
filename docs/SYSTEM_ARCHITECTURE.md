# System Architecture

## Proposed flow
1. Hopper receives manually sorted-safe feed.
2. Vibrating tray loosens/spreads items; it does not guarantee single-item separation.
3. Conveyor transports items through the inspection zone.
4. IR/photoelectric beam detects arrival and triggers a camera capture; it does not identify material.
5. RGB camera and YOLO detect visible object classes.
6. Inductive, load-cell and moisture readings provide supporting features.
7. A Python Random Forest model fuses structured features.
8. A conservative decision policy routes uncertain or conflicting readings to manual inspection.
9. A suitable multi-position diverter routes accepted items under supervision.
10. Bin-level sensors report fill status.

## Sensor roles and limitations
| Element | Role | Limitation |
|---|---|---|
| RGB camera | Visible appearance | Cannot see hidden composition |
| IR/photoelectric | Arrival and timing | Presence only |
| Inductive | Conductive metal clue | Not exact alloy or e-waste identification |
| Load cell + HX711 | Mass | Use a static weigh station |
| Moisture | Supporting wetness feature | Wet contamination can mislead |
| Ultrasonic/ToF | Distance/bin fill | Not material identification |
| Gate limit switch | Gate position feedback | Does not verify correct material |

## Position tracking
A camera-to-diverter transport delay must be calibrated at operating speed. An encoder or additional photoelectric sensors can improve tracking. Overlapping items need to be detected and held for manual inspection.

## Routing
One servo flap cannot independently route eight categories. A real design requires a suitable indexed chute, multiple gates or another engineered routing mechanism, with position feedback and safe guarding.

## Fail-safe behaviour
Hold/manual inspection on low confidence, sensor disagreement, unknown class, sensor fault, full destination bin, jam or communication loss. A software flag is not a substitute for a physical emergency-stop safety circuit.
