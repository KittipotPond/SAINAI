from ultralytics import YOLO

model = YOLO(r"C:\Users\kitti\OneDrive\Sainai Coding\SAINAI\runs\detect\train8\weights\best.onnx")

model.predict(r"C:\Users\kitti\OneDrive\Sainai Coding\SAINAI\Licenseplate\train\images\0A444D8C-6C29-4513-BB48-7DDDBB48DFB0_png.rf.bf03fc28cb6806b2cb93edf47e9b97a8.jpg",
              save=True,
              conf=0.5)