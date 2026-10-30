#include "HX711.h"
// Replace placeholder calibration factor after calibration using known masses.
HX711 scale;
constexpr int DOUT_PIN = 32, SCK_PIN = 33;
float CALIBRATION_FACTOR = -7050.0f;
void setup() {
  Serial.begin(115200);
  scale.begin(DOUT_PIN, SCK_PIN);
  scale.set_scale(CALIBRATION_FACTOR);
  scale.tare();
}
void loop() {
  if (scale.is_ready()) {
    float grams = scale.get_units(5);
    Serial.printf("{\"sensor\":\"load_cell\",\"weight_g\":%.2f}\n", grams);
  } else Serial.println("{\"sensor\":\"load_cell\",\"error\":\"not_ready\"}");
  delay(500);
}
// Weigh at a stationary/paused station; belt vibration corrupts readings.
