

import cv2 
import numpy as np 
import random 

def encrypt(): 
	img1 = cv2.imread('figs/cow1.jpg') 
	img2 = cv2.imread('figs/camel1.jpg') 
	
	for i in range(img2.shape[0]): 
		for j in range(img2.shape[1]): 
			for l in range(3): 
				
				v1 = format(img1[i][j][l], '08b') 
				v2 = format(img2[i][j][l], '08b') 
				
				v3 = v1[:4] + v2[:4] 
				
				img1[i][j][l]= int(v3, 2) 
				
	cv2.imwrite('outputs/camel1-in-cow1.png', img1) 

	
def decrypt(): 
	img = cv2.imread('outputs/camel1-in-cow1.png') 
	width = img.shape[0] 
	height = img.shape[1] 
	
	img1 = np.zeros((width, height, 3), np.uint8) 
	img2 = np.zeros((width, height, 3), np.uint8) 
	
	for i in range(width): 
		for j in range(height): 
			for l in range(3): 
				v1 = format(img[i][j][l], '08b') 
				v2 = v1[:4] + chr(random.randint(0, 1)+48) * 4
				v3 = v1[4:] + chr(random.randint(0, 1)+48) * 4
				
				img1[i][j][l]= int(v2, 2) 
				img2[i][j][l]= int(v3, 2) 
	
	cv2.imwrite('outputs/cow1-after.png', img1) 
	cv2.imwrite('outputs/camel1-after.png', img2) 
	
	
encrypt() 
decrypt() 
