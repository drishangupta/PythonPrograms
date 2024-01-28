def YoloM():
    from ultralytics import YOLO

    # Load a model
    model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)

    # Train the model
    results = model.train(data='C:\\Users\\drish\\PythonPrograms\\datasets\\VehicleClassificationV2.v3i.yolov8\\data.yaml', epochs=15, imgsz=640)
if __name__=="__main__":
    YoloM()