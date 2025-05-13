import cv2
from matplotlib import pyplot as plt

# normalized values for image in line 8
x_center, y_center, width, height = 0.6783, 0.5766, 0.1242, 0.10975

# load image
image = cv2.imread('/Users/yejinshin/Downloads/sml312/datasets/ramp_dataset/images/val/img005.jpg')
h, w = image.shape[:2]

# normalized --> actual pixel value
x_center_pixel = int(x_center * w)
y_center_pixel = int(y_center * h)
width_pixel = int(width * w)
height_pixel = int(height * h)

x1 = int(x_center_pixel - width_pixel / 2)
y1 = int(y_center_pixel - height_pixel / 2)
x2 = int(x_center_pixel + width_pixel / 2)
y2 = int(y_center_pixel + height_pixel / 2)

# draw rectangle
cv2.rectangle(image, (x1, y1), (x2, y2), color=(0, 255, 0), thickness=2)


# display w/ matplotlib
plt.figure(figsize=(10, 6))
plt.imshow(image)
plt.axis('off')
plt.tight_layout()
plt.show()