from ultralytics import YOLO
from ultralytics.data.augment import AlbumentationsTransform
import albumentations as A

# Augmentations to be applied to images
transform = AlbumentationsTransform(
    A.Compose([
        A.HorizontalFlip(p=0.5),
        A.VerticalFlip(p=0.2),
        A.RandomBrightnessContrast(p=0.2),
        A.ShiftScaleRotate(shift_limit=0.05, scale_limit=0.1, rotate_limit=10, p=0.3),
        A.MotionBlur(p=0.1)
    ]),
    bbox_format='yolo'
)

# Trains with custom parameters & albumentations, augments the dataset
model = YOLO("yolo11n.pt")
model.train(
    data="ramp_dataset.yaml",
    epochs=800,
    imgsz=640,
    batch=4,
    lr0=0.001,
    optimizer='SGD',
    patience=30,
    augment=True,
    transforms=transform
)
