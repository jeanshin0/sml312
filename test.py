# 1) Install prerequisites:
#    pip install ultralytics opencv-python

from ultralytics import YOLO
import os
import cv2

# 2) Load your custom YOLOv8 model
#    (replace with the path to your trained ramp-detector)
model = YOLO('/Users/yejinshin/Downloads/sml312/runs/detect/train/weights/best.pt')

# 3) Set up your image directory and output directory
image_dir  = '/Users/yejinshin/Downloads/sml312/datasets/ramp_dataset/images/val'
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

# 4) Loop over images, run inference, check for ramps, and save visualized results
for img_name in os.listdir(image_dir):
    if not img_name.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue

    img_path = os.path.join(image_dir, img_name)
    # Run inference (returns a list of Results; we only have one image → take [0])
    results = model(img_path)[0]

    # Filter detections whose class name is 'ramp'
    ramp_boxes = [
        box for box, cls in zip(results.boxes, results.boxes.cls)
        if model.names[int(cls)] == 'ramp'
    ]

    if ramp_boxes:
        print(f"{img_name}: RAMP detected")
        # Draw boxes on the image
        img = cv2.imread(img_path)
        for box in ramp_boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        # Save annotated image
        cv2.imwrite(os.path.join(output_dir, img_name), img)
    else:
        print(f"{img_name}: no ramp detected")
