// Detects suitable conductive metal nearby, not alloy or e-waste identity.
// Ensure sensor output is level-shifted/isolated; never connect 12/24V to ESP32.
const int SENSOR_PIN = 25;
void setup() { Serial.begin(115200); pinMode(SENSOR_PIN, INPUT_PULLUP); }
void loop() {
  bool detected = digitalRead(SENSOR_PIN) == LOW;
  Serial.printf("{\"sensor\":\"inductive\",\"metal_detected\":%s}\n", detected ? "true" : "false");
  delay(250);
}
