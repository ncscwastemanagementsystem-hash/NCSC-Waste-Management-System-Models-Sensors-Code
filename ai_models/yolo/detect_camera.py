"""YOLO webcam/file inference. Requires custom trained waste-detection weights."""
import argparse
from ultralytics import YOLO

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--weights", required=True, help="Path to trained .pt weights")
    p.add_argument("--source", default="0", help="Camera index or image/video path")
    p.add_argument("--conf", type=float, default=0.50)
    p.add_argument("--imgsz", type=int, default=640)
    a = p.parse_args()
    source = int(a.source) if a.source.isdigit() else a.source
    YOLO(a.weights).predict(source=source, conf=a.conf, imgsz=a.imgsz, show=True, save=True)

if __name__ == "__main__":
    main()
