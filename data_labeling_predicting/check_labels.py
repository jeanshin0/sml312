import os
import glob
import cv2
import numpy as np
from matplotlib import pyplot as plt

# manually check dataset
images_dir = '/Users/yejinshin/Downloads/sml312/datasets/ramp_dataset/images/val'
labels_dir = '/Users/yejinshin/Downloads/sml312/datasets/ramp_dataset/labels/val'

count = 0

for pattern in ['*.jpg', '*.jpeg', '*.png']:
    for img_path in glob.glob(os.path.join(images_dir, pattern)):
        # builds path
        base = os.path.splitext(os.path.basename(img_path))[0]
        lbl_path = os.path.join(labels_dir, base + '.txt')

        # loads image & presets it
        image = cv2.imread(img_path)
        if image is None:
            continue
        h, w = image.shape[:2]

        # draw each bbox if there is a class label within the image
        if os.path.exists(lbl_path):
            with open(lbl_path, 'r') as f:
                for line in f.read().strip().splitlines():
                    parts = line.split()
                    if len(parts) != 5:
                        continue
                    class_id, x_c, y_c, bw, bh = map(float, parts)
                    x_center = int(x_c * w)
                    y_center = int(y_c * h)
                    box_w    = int(bw  * w)
                    box_h    = int(bh  * h)
                    x1 = x_center - box_w  // 2
                    y1 = y_center - box_h  // 2
                    x2 = x_center + box_w  // 2
                    y2 = y_center + box_h  // 2

                    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(
                        image, str(int(class_id)),
                        (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 
                        0.5, (0, 255, 0), 1, cv2.LINE_AA
                    )
        else:
            print(f"ℹ️  No label for {base}")

        # Display image with matplotlib
        plt.figure(figsize=(8, 5))
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        plt.title(base)
        plt.show()
        count+=1
    
print(count)