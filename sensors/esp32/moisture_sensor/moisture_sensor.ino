// Raw ADC output only; not a calibrated moisture percentage.
// Confirm module output voltage is safe for the ESP32 ADC before wiring.
const int MOISTURE_PIN = 34;
void setup() { Serial.begin(115200); analogReadResolution(12); }
void loop() {
  int raw = analogRead(MOISTURE_PIN);
  Serial.printf("{\"sensor\":\"moisture\",\"raw_adc\":%d}\n", raw);
  delay(500);
}
