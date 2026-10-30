/*
 ESP32 servo diverter demonstration only.
 Serial: GATE <angle 0..180> or STOP.
 Not an integrated conveyor controller or certified safety system.
 Add qualified physical E-stop circuit, gate limit feedback, guarded mechanics,
 motor-driver protection and fail-safe power design before deployment.
*/
#include <ESP32Servo.h>
constexpr int SERVO_PIN = 18;
constexpr int ESTOP_PIN = 27; // Connect through a suitable normally-closed interface.
constexpr int HOME_ANGLE = 90;
Servo gate;
bool stopped = false;
void stopGate() { stopped = true; gate.write(HOME_ANGLE); }
void setup() {
  Serial.begin(115200);
  pinMode(ESTOP_PIN, INPUT_PULLUP);
  gate.setPeriodHertz(50);
  gate.attach(SERVO_PIN, 500, 2400);
  gate.write(HOME_ANGLE);
  Serial.println("{\"status\":\"ready_demo\",\"automatic_routing\":false}");
}
void loop() {
  if (digitalRead(ESTOP_PIN) == LOW) {
    stopGate();
    Serial.println("{\"status\":\"estop_active\"}");
  }
  if (!Serial.available()) return;
  String cmd = Serial.readStringUntil('\n'); cmd.trim();
  if (cmd == "STOP") { stopGate(); Serial.println("{\"status\":\"stopped\"}"); return; }
  if (stopped) { Serial.println("{\"error\":\"operator_check_required\"}"); return; }
  if (cmd.startsWith("GATE ")) {
    int angle = cmd.substring(5).toInt();
    if (angle < 0 || angle > 180) { Serial.println("{\"error\":\"angle_out_of_range\"}"); return; }
    gate.write(angle);
    Serial.printf("{\"status\":\"demo_gate_commanded\",\"angle\":%d}\n", angle);
  } else Serial.println("{\"error\":\"unknown_command\"}");
}
