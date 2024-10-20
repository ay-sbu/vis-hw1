
import cv2
  
image = cv2.imread('figs/camel1.jpg')

font = cv2.FONT_HERSHEY_SIMPLEX
org = (100, 100)
fontScale = 3
color = (0, 0, 255) # BGR
thickness = 2
 
image = cv2.putText(image, 'Salam Goodarz', org, font, 
                   fontScale, color, thickness, cv2.LINE_AA)
 
cv2.imwrite("outputs/camel-text.jpg", image) 
  