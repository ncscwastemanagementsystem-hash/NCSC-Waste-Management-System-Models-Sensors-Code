from software.decision_policy import decide

def test_low_confidence_holds():
    d = decide("plastic", 0.55, False)
    assert d.action == "HOLD" and d.category == "manual_inspection"

def test_sensor_disagreement_holds():
    d = decide("paper_cardboard", 0.95, True)
    assert d.category == "manual_inspection"

def test_estop_stops():
    assert decide("metal", 0.99, True, emergency_stop=True).action == "STOP"

def test_hazardous_item_isolated():
    assert decide("plastic", 0.99, False, hazardous_flag=True).action == "ISOLATE"

def test_route_requires_supervision():
    assert decide("plastic", 0.95, False).action == "ROUTE_SUPERVISED"
