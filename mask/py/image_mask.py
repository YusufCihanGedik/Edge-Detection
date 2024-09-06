import cv2
import numpy as np

img = cv2.imread(r"/home/gedik/Desktop/mask/mask_crop.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

lower_bound = 110  # Beyaz tonlarının alt limiti
upper_bound = 255  # Beyaz tonlarının üst limiti

mask = cv2.inRange(gray, lower_bound, upper_bound)

cv2.imshow("mask",mask)
result = cv2.bitwise_and(img, img, mask=mask)

# Sonuçları göster
cv2.imshow('Original Image', img)
cv2.imshow('Detected White Tones', result)
cv2.imwrite(r"/home/gedik/Desktop/mask/detected_white_tones.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()