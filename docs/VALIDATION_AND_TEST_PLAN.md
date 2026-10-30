# Validation and Test Plan

## AI data protocol
1. Define label instructions and edge cases before annotation.
2. Collect varied examples: clean/dirty, wet/dry, crushed/intact, lighting variation and local waste types.
3. Split by physical item or collection session before augmentation to avoid near-duplicate leakage.
4. Keep a locked final test set untouched until model selection is complete.
5. Record camera, lighting, sensor calibration, model version and collection date.

## Metrics
- Per-class precision, recall and F1
- Macro and weighted averages
- Confusion matrix
- Reject/manual-inspection rate
- Performance by lighting and contamination subgroup
- Confidence calibration
- Physical routing success and misroute rate, reported separately

An 80% overall accuracy can be a proposed minimum project target, not an achieved result. Overall accuracy can hide poor performance on rare or hazardous classes.

## Hardware commissioning evidence
| Test | Method | Evidence to retain |
|---|---|---|
| IR trigger | Repeated passes at known spacing | Trigger count and timing log |
| Load cell | Zero and known masses | Calibration error |
| Inductive | Known metal/non-metal samples | Detection table |
| Moisture | Controlled samples | Repeatability and limitations |
| Bin level | Known distances/fill heights | Error range |
| Gate | Repeated no-load/test-load cycles | Position feedback and repeatability |
| E-stop | Trigger during supervised test | Safe removal of motion energy |
| Jam/full-bin | Safely simulate | Hold state and alert |
| Power loss | Remove control power safely | No unexpected restart |

Do not mark a test passed without collected evidence.
