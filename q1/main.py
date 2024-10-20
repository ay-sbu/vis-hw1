import cv2

def write_hidden_message():
    image = cv2.imread('figs/camel-low-contrast.jpg')
    x, y = 720, 50
    hidden_text = 'SALAM'

    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (x, y)
    fontScale = 2
    color = (int(image[y, x][0]), int(image[y, x][1]), int(image[y, x][2]))
    # color = (255,0,0)
    print("text color:", color)
    thickness = 1
    
    image = cv2.putText(image, hidden_text, org, font, 
                    fontScale, color, thickness, cv2.LINE_AA)
    
    # cv2.line(image, (x, y+15), (x+200, y+15), (0,0,255), 3)
    
    cv2.imwrite("figs/camel-hidden-text.jpg", image) 

def find_hidden_message():
    img = cv2.imread('figs/camel-hidden-text.jpg', cv2.IMREAD_GRAYSCALE)
    equalized_img = cv2.equalizeHist(img)
    cv2.imwrite("figs/found-text.jpg", equalized_img) 
    

write_hidden_message()
find_hidden_message()