#include <ESP32Servo.h>
// Bench test only; guard pinch points and use a suitable separate servo supply.
Servo testServo;
const int SERVO_PIN = 18;
void setup() { Serial.begin(115200); testServo.attach(SERVO_PIN, 500, 2400); }
void loop() {
  testServo.write(60); delay(1000);
  testServo.write(90); delay(1000);
  testServo.write(120); delay(1000);
  testServo.write(90); delay(1000);
}
