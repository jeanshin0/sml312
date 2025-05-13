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

yolo task=detect mode=train \
     model= yolo11s.pt \
     data=ramp_dataset.yaml \
     epochs=800 \
     imgsz=640 \
     optimizer=SGD \
     batch=1 \
     lr0=0.01 \
     lrf=0.1 \
     momentum=0.937 \
     weight_decay=0.0005 \
     augment=True \
     device=cpu

yolo task=detect mode=train \
    model=/Users/yejinshin/Downloads/sml312/yolo11n.pt \
    data=ramp_dataset.yaml \
    epochs=400 \                         # Lower to 400 (based on early decay)
    imgsz=640 \
    optimizer=AdamW \                    # Switch from SGD to AdamW
    lr0=0.005 \                          # Lower initial learning rate
    lrf=0.01 \                           # Much smaller final LR for smoother decay
    weight_decay=0.001 \                # Slightly stronger regularization
    momentum=0.9 
    patience=50 \
    augment=True \
    device=cpu

