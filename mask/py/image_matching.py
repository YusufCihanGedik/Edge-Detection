# import cv2
# import numpy as np

# # Orijinal görüntü ve maskeyi yükle
# original_img = cv2.imread(r"canny_images.jpg")
# mask_img = cv2.imread(r"mask.jpg", cv2.IMREAD_GRAYSCALE)

# # Mask'i renkli hale getir (üzerine renk işlemleri yapabilmek için)
# mask_colored = cv2.cvtColor(mask_img, cv2.COLOR_GRAY2BGR)

# # Aynı boyutta olup olmadığını kontrol edin
# if original_img.shape[:2] != mask_img.shape[:2]:
#     print("Error: Mask and original image must have the same dimensions.")
#     exit()

# # Boş bir görüntü oluştur (sonucu göstermek için)
# result_img = original_img.copy()

# # Mask'teki beyaz (255) piksellerin olduğu yerlere bak ve karşılaştır
# # Eşleşen pikselleri yeşil, eşleşmeyenleri kırmızı yapacağız
# for y in range(mask_img.shape[0]):
#     for x in range(mask_img.shape[1]):
#         if mask_img[y, x] == 255:  # Maske pikselleri beyaz (255) ise
#             if np.array_equal(original_img[y, x], [255, 255, 255]):  # Orijinalde de beyazsa
#                 result_img[y, x] = [0, 255, 0]  # Eşleşen piksekkkklleri yeşil yap
#             else:
#                 result_img[y, x] = [0, 0, 255]  # Eşleşmeyen pikselleri kırmızı yap

# # Sonucu göster ve kaydet
# cv2.imshow('Comparison Result', result_img)
# cv2.imwrite('comparison_result.jpg', result_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()





import cv2
import numpy as np

# Orijinal görüntü ve Canny kenar görüntüsünü yükleyin
original_img1 = cv2.imread(r"detected_white_tones.jpg")  # Orijinal görüntü
original_img = cv2.imread(r"orginal.jpg")
gray_original = cv2.cvtColor(original_img1, cv2.COLOR_BGR2GRAY)  

t_lower = 100  
t_upper = 200  
canny_output = cv2.Canny(gray_original, t_lower, t_upper)

result_img = original_img.copy()

result_img[canny_output != 0] = [255, 0, 0]  # Yeşil (RGB: 0, 255, 0)

# Sonuçları göster ve kaydet
cv2.imshow('Canny Edges on Original Image', result_img)
cv2.imshow('Canny ', canny_output)

cv2.imwrite('final.jpg', result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
