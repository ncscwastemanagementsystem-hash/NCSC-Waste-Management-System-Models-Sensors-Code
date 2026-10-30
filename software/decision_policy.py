"""Example routing gate; not a certified or complete machine-safety system."""
from dataclasses import dataclass

@dataclass
class Decision:
    action: str
    category: str
    reason: str

def decide(category: str, confidence: float, metal_detected: bool,
           sensor_fault: bool = False, bin_full: bool = False,
           emergency_stop: bool = False, hazardous_flag: bool = False,
           threshold: float = 0.80) -> Decision:
    if emergency_stop:
        return Decision("STOP", "reject", "Emergency stop active")
    if sensor_fault:
        return Decision("HOLD", "manual_inspection", "Sensor fault")
    if bin_full:
        return Decision("HOLD", "manual_inspection", "Destination bin full")
    if hazardous_flag:
        return Decision("ISOLATE", "manual_inspection", "Potential hazardous item")
    if not 0 <= confidence <= 1 or confidence < threshold:
        return Decision("HOLD", "manual_inspection", "Low or invalid confidence")
    if category in {"manual_inspection", "reject"}:
        return Decision("HOLD", category, "Model requested manual handling")
    if metal_detected and category not in {"metal", "e_waste"}:
        return Decision("HOLD", "manual_inspection", "Visual/sensor disagreement")
    return Decision("ROUTE_SUPERVISED", category, "Passed example policy; operator supervision required")
