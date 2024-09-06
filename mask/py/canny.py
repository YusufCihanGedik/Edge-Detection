import cv2
import numpy as np
import os

img = cv2.imread(r"detected_white_tones.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

t_lower = 100  # Alt eşik değeri
t_upper = 200  # Üst eşik değeri
aperture_size = 5  # Canny için Sobel'in büyüklüğü
L2Gradient = True

canny_output = cv2.Canny(img, t_lower, t_upper, apertureSize=aperture_size, L2gradient=L2Gradient)

img_edges = cv2.bitwise_and(img, img, mask=canny_output)

cv2.imshow('Canny with Threshold', img_edges)

output_dir = r"/home/gedik/Desktop/mask"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

cv2.imwrite(os.path.join(output_dir, "canny_images.jpg"), img_edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
