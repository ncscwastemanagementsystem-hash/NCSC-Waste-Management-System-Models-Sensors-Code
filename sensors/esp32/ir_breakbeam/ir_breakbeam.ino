// Presence/timing only; this sensor does not identify material.
const int BEAM_PIN = 26;
void setup() { Serial.begin(115200); pinMode(BEAM_PIN, INPUT_PULLUP); }
void loop() {
  static int previous = HIGH;
  int state = digitalRead(BEAM_PIN);
  if (state != previous) {
    Serial.printf("{\"sensor\":\"ir_breakbeam\",\"blocked\":%s}\n", state == LOW ? "true" : "false");
    previous = state;
  }
  delay(10);
}
