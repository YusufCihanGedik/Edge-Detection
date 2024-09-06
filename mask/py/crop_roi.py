# import cv2 
# img = cv2.imread(r"mask.jpg")
# height, width, _ = img.shape
# print(img.shape)
# # x,y,w,h = 102 , 96 , 2428 , 2430
# # x1,y1,w1,h1 = 0 , 0 , 50 , 2650
# # x2,y2,w2,h2 = 0 , 0 , 2650 , 50
# # x3,y3,w3,h3 = 2590 , 0 , 500 , 0
# x, y, w, h = 102, 103, 2415, 2420
# x1, y1, w1, h1 = 0, 0, 50, height  # Sol kenar
# x2, y2, w2, h2 = 0, 0, width, 30  # Üst kenar
# x3, y3, w3, h3 = width - 50, 0, 50, height  # Sağ kenar (sağdan 50px genişliğinde)
# x4, y4, w4, h4 = 0, height-11, width, 11 
# roi = img[y:y+h, x:x+w]
# img[y:y+h, x:x+w] =(0,0,0)
# img[y1:y1+h1, x1:x1+w1] =(0,0,0)
# img[y2:y2+h2, x2:x2+w2] =(0,0,0)
# img[y3:y3+h3, x3:x3+w3] =(0,0,0)
# img[y4:y4+h4, x4:x4+w4] =(0,0,0)
# cv2.imwrite(r"mask_crop.jpg",img)
# # cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

