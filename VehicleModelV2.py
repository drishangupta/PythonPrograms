def YoloMe():
    from ultralytics import YOLO

    # Load a model
    model = YOLO('DroneDetect.pt')  # load a pretrained model (recommended for training)

    # Train the model
    results = model.train(data='C:/Users/drish/PythonPrograms/datasets/Vehicles-OpenImages.v1-416x416.yolov8/data.yaml', epochs=30, imgsz=640)
if __name__=="__main__":
    YoloMe()