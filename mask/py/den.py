import numpy as np 
import cv2

img = cv2.imread(r"/home/gedik/Desktop/mask/Image_20240905124647329.bmp")


img_shape = img.shape
print(img_shape)


x, y, w, h = 2100, 440, 2650, 2590  

cropped_region = img[y:y+h, x:x+w]
cropped_region2 = cv2.imread(r"mask_black_inside_white_outside.jpg")


black_background = np.ones(img_shape,dtype=np.uint8)*255
# cv2.imshow("Cropped Region", cropped_region)

black_background[y:y+h, x:x+w] = cropped_region2


cv2.imwrite(r"/home/gedik/Desktop/mask/white_background.jpg", black_background)

cv2.imwrite(r"/home/gedik/Desktop/mask/mask.jpg", cropped_region)
# cv2.imshow("img",cv2.resize(img,(1080,720)))
cv2.waitKey(0)
cv2.destroyAllWindows()