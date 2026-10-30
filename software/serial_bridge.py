"""Read newline-delimited JSON telemetry from an ESP32 serial port."""
import argparse
import json
import serial

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--port", required=True, help="COM4 or /dev/ttyUSB0")
    p.add_argument("--baud", type=int, default=115200)
    a = p.parse_args()
    with serial.Serial(a.port, a.baud, timeout=1) as ser:
        print(f"Listening on {a.port} at {a.baud}")
        while True:
            line = ser.readline().decode("utf-8", errors="replace").strip()
            if not line:
                continue
            try:
                print(json.dumps(json.loads(line), ensure_ascii=False))
            except json.JSONDecodeError:
                print("Non-JSON serial:", line)

if __name__ == "__main__":
    main()
