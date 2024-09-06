# import cv2
# import numpy as np

# # Görseli yükle
# img_path = "/home/gedik/Desktop/mask/mask.jpg"
# img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# # Görseli binarize et (siyah-beyaz yapmak için)
# _, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)


# # Dış sınırları tespit et
# contours, _ = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Maske oluştur ve sınırların içini beyaz, dışını siyah yap
# mask = np.ones_like(img)*255
# cv2.drawContours(mask, contours, -1, 0, thickness=cv2.FILLED)

# # Maske dışındaki alanı siyah yap
# result = np.ones_like(img) * 255  # Beyaz bir görüntü oluştur
# result[mask == 0] = 0  # Beyaz sınırların dışını siyah yap

# # Sonucu kaydet
# output_path = "output_image.jpg"
# cv2.imwrite(output_path, result)

# output_path



import numpy as np
import cv2

img = cv2.imread(r"/home/gedik/Desktop/mask/mask.jpg", cv2.IMREAD_GRAYSCALE)

_, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

mask = np.ones_like(img) * 255  # Tamamen beyaz bir maske (255 beyaz)

cv2.drawContours(mask, contours, -1, 0, thickness=cv2.FILLED)

cv2.imwrite(r"/home/gedik/Desktop/mask/mask_black_inside_white_outside.jpg", mask)

# Eğer sonucu göstermek istersen (opsiyonel)
# cv2.imshow("Mask", mask)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
