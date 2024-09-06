import numpy as np
import cv2

# Görselleri yükleyin
image_full = cv2.imread('/home/gedik/Desktop/mask/mask.jpg', cv2.IMREAD_GRAYSCALE)
image2_full = cv2.imread('/home/gedik/Desktop/mask/Image_20240905124647329.bmp', cv2.IMREAD_GRAYSCALE)

# Crop işlemi için x, y, w, h koordinatları
x, y, w, h = 2100, 440, 2650, 2590

# Tam görselleri crop yapın
image = image_full[y:y+h, x:x+w]
image2 = image2_full[y:y+h, x:x+w]

# Görüntünün boyutlarını alın
height, width = image.shape

# Yeni bir boş görüntü oluşturun
diff_image = np.zeros((height, width), dtype=np.uint8)
diff_image2 = np.zeros((height, width), dtype=np.uint8)
diff_image_right_raw = np.zeros((height, width), dtype=np.uint8)
diff_image_right_raw2 = np.zeros((height, width), dtype=np.uint8)

# İlk fark hesaplaması
for y in range(height):
    for x in range(1, width - 1):  # İlk ve son sütun işlem dışı bırakılır
        if image[y, x-1] != 0 and image[y, x+1] != 0:
            diff_image[y, x] = np.abs(int(image[y, x-1]) - int(image[y, x+1]))

# 4 piksel sonrası için fark hesaplaması
for y in range(height):
    for x in range(width):  # Tüm sütunlar üzerinde döngü
        if x < width - 4:  # En az 4 piksel sonrasına kadar olan değerlere bak
            if image[y, x] != 0 and image[y, x+4] != 0:  # 0 piksel değerlerini atla
                diff_image_right_raw[y, x+2] = np.abs(int(image[y, x]) - int(image[y, x+4]))

# Kenarların tespiti ve işaretlenmesi
diff_image_left = diff_image.copy()
image_right = image.copy()

for y in range(height):
    max_x = np.argmax(image[y, :])  
    image[y, max_x] = 255 
    diff_image_left[y, max_x+1:] = 0  
    diff_image_right_raw[y, :max_x+1] = 0  
    image[y, :max_x+1] = 0  

for y in range(height):
    non_zero_indices = np.where(image[y, :] != 0)[0]
    if non_zero_indices.size > 0:
        min_x = np.min(non_zero_indices)
        max_x = np.max(non_zero_indices)
        middle_x = (min_x + max_x) // 2
        diff_image_right_raw[y, :middle_x+1] = 0

image_right_2 = image.copy()

# Farkların en yüksek olduğu pikselleri işaretleme
for y in range(height):
    max_x = np.argmax(diff_image_left[y, :])
    diff_image2[y, max_x] = 255

for y in range(height):
    max_x = np.argmax(diff_image_right_raw[y, :])
    diff_image_right_raw2[y, max_x] = 255

# Görseli renkli formata çevirme
color_image = cv2.cvtColor(image2, cv2.COLOR_GRAY2BGR)

# Tespit edilen kenarları kırmızı renkte işaretleme
color_image[diff_image2 == 255] = (0, 0, 255)
color_image[diff_image_right_raw2 == 255] = (0, 0, 255)

# Sonuç görüntülerini gösterin ve kaydedin
cv2.imshow('Difference Image', diff_image[0:100, :])
cv2.imshow('Difference Image2', diff_image_right_raw[0:100, :])
cv2.imshow('Original Image with Red Highlights', color_image)
cv2.imshow('Original Image', image[0:100, :])

cv2.imwrite('image_righ2t.png', color_image)
cv2.imwrite('image_right_3.png', image_right_2)

cv2.waitKey(0)
cv2.destroyAllWindows()
