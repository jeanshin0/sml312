import cv2
import numpy as np
import os

def boundary(path):
    print(path + "\n")
    # loads image w/ boundary box
    img = cv2.imread(path)
    h_img, w_img = img.shape[:2]

    # from box extract anything red (indicated by red box)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # find ranges of box
    lower1 = np.array([0, 70, 50])
    upper1 = np.array([10, 255, 255])
    lower2 = np.array([170, 70, 50])
    upper2 = np.array([180, 255, 255])
    mask1 = cv2.inRange(hsv, lower1, upper1)
    mask2 = cv2.inRange(hsv, lower2, upper2)
    mask = cv2.bitwise_or(mask1, mask2)

    # contours the box
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # find square
    cnt = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(cnt)

    # normalize values
    x_center = (x + w/2) / w_img
    y_center = (y + h/2) / h_img
    w_norm    = w / w_img
    h_norm    = h / h_img

    class_id = 0
    
    # print value associated to class
    print(f"{class_id} {x_center:.6f} {y_center:.6f} {w_norm:.6f} {h_norm:.6f}")


# point this to your images folder
IMAGE_DIR = '/Users/yejinshin/Downloads/sml312/check'

# list everything in that folder…
for fname in os.listdir(IMAGE_DIR):
    # …but only keep common image extensions
    if not fname.lower().endswith(('.png', '.jpg', '.jpeg')):  
        continue

    full_path = os.path.join(IMAGE_DIR, fname)
    boundary(full_path)