# Wheelchair Accessibility Classification / Detection using YOLO Methodology

This project aims to detect ramps & stairs in environments using YOLOv11/v8(s & n), as part of a broader effort to assess wheelchair accessibility across different locations in Korea.

## Project Structure
### `data_labeling_predicting/` – Helper Functions
- `check_labels.py` – Consistency check to ensure images have properly labelled classes
- `redbox.py` – Subfunction of check_labels to draw in the redboxes, given label & normalized boundary box values
- `drawbox.py` – Obtains normalized values from images with unlabelled boundary boxes
- `plot_model_prediction.py` – Visualizes particular YOLO model predictions

### `datasets/ramp_dataset/` – Dataset (YOLO Format)
- `images/train/` – Training images ~48
- `images/val/` – Validation images ~14
- `labels/train/` – Normalized YOLO format labels for training 
- `labels/val/` – Normalized YOLO format labels for validation  
- `train.cache` – Trained cached images/dataset for faster training
- `val.cache` – Validation cached images/dataset for faster training

### `runs/` – YOLO Training / Model Outputs
- `detect/` – Default model output directory
- `detect/train/` to `train21/` – Saved from training runs  

### `yolo_models_training/` – Training Scripts, YAML Config, & Models
- `ramp_dataset.yaml` – Personalized config file to identify ramp / stair classes
- `train.py` – Training script to train model
- `yolo11n.pt` – YOLOv11 nano model 
- `yolo11s.pt` – YOLOv11 small model
- `yolov8n.pt` – YOLOv8 nano model

### Other Files
- `README.md` – Project documentation  
- `ramp_dataset.yaml_ex` – Sample config file

## YAML Configuration
To run YOLO scripts, a YAML file needs to be properly configured, ensuring paths & classes are accurately labelled.


## Model Overview
This project utilizes three different models to:

1. identify ramps (class 0) and stairs (class 1), and

2. determine which model performs best given our dataset.

`yolo11n.pt`: Nano version (fastest, smallest)

`yolo11s.pt`: Small version (better accuracy)

`yolov8n.pt`: YOLOv8 model for comparison


## How to Run

You can train the model in two ways:

### Option 1: Python Script  
Run the python training script directly. Modify parameters inside `./yolo_models_training/train.py` if needed:

```bash
python train.py
```
### Option 2: YOLO Bash Script  
Run the following bash script in `./yolo_models_training` directory
```bash
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
```

## Training Results
Training outputs are saved in:

`runs/detect/trainXX/`

Each subfolder contains logs, weights, and many other plots.
