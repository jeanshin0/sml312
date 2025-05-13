from ultralytics import YOLO
from matplotlib import pyplot as plt
import cv2

# Utilizes current best image
model = YOLO('/Users/yejinshin/Downloads/sml312/runs/detect/train21/weights/best.pt')

image = cv2.imread('/Users/yejinshin/Downloads/sml312/datasets/ramp_dataset/images/val/img013.jpg')

results = model(image)

annotated_image = results[0].plot()

# 
annotated_rgb = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 6))
plt.imshow(annotated_rgb)
plt.axis('off')
plt.tight_layout()
plt.show()