from ultralytics import YOLO

model = YOLO("yolov8n.yaml")

model = YOLO("yolov8n.pt")

path = r"C:\Users\kitti\OneDrive\Sainai Coding\SAINAI\Licenseplate\data.yaml"
results = model.train(data=path, epochs=10)

results = model.val()

success = model.export(format='onnx')
