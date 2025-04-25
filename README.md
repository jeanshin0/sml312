# Classification

- see if it is wheelchair accessible

- 

yolo task=detect mode=train \
     model=yolov8n.pt \
     data=ramp_dataset.yaml \
     epochs=1000 \
     imgsz=640 \
     augment=True

<class_id> <x_center> <y_center> <width> <height>