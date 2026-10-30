// HC-SR04-style example. ECHO is often 5V: use divider/level shifter for ESP32.
const int TRIG_PIN = 5, ECHO_PIN = 18;
void setup() { Serial.begin(115200); pinMode(TRIG_PIN, OUTPUT); pinMode(ECHO_PIN, INPUT); }
void loop() {
  digitalWrite(TRIG_PIN, LOW); delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH); delayMicroseconds(10); digitalWrite(TRIG_PIN, LOW);
  unsigned long duration = pulseIn(ECHO_PIN, HIGH, 30000);
  if (!duration) Serial.println("{\"sensor\":\"bin_level\",\"error\":\"timeout\"}");
  else {
    float cm = duration * 0.0343f / 2.0f;
    Serial.printf("{\"sensor\":\"bin_level\",\"distance_cm\":%.1f}\n", cm);
  }
  delay(500);
}
