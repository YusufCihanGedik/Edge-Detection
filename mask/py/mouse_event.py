import cv2 


img = cv2.imread(r"mask.jpg")


cv2.imshow('image', img) 

def mouse_click(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN: 
        print(x,y)

cv2.setMouseCallback('image', mouse_click) 
   
cv2.waitKey(0) 
  
# close all the opened windows. 
cv2.destroyAllWindows() 