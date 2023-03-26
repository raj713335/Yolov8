from ultralytics import YOLO

model = YOLO()

model.train(data='data.yaml', epochs=200)

#  yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=100 imgsz=640