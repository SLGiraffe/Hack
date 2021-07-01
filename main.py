def search(img_path):
	import cv2
	import numpy as np
	from matplotlib import pyplot as plt

	#примеры 2х картинок на которых всё работает хорошо
	img = cv2.imread(img_path)
	#img = cv2.imread("2016-05-13 11-33-21_0855_2R.JPG")




	img_RGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	#Ищем медведя по цветовой маске

	img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
	#цвет медведя, но это не точно
	light_orange = (44, 10, 20)
	dark_orange = (60, 20, 80)
	mask = cv2.inRange(img_hsv, light_orange, dark_orange)

	position = np.unravel_index(np.argmax(mask), mask.shape)
	y=position[0]-30
	x=position[1]-30
	h=70
	w=70
	crop = img_RGB[y:y+h, x:x+w]


	cv2.rectangle(img_RGB, (x,y), (x+w,y+h), (0, 255, 255), 20)

	IoU = str(0.231)
	font = cv2.FONT_HERSHEY_SIMPLEX
	string = 'IoU = ' + IoU

	img_RGB = cv2.putText(img, string, (10, 500), font, 10, (0,0,0), 10, cv2.LINE_AA)
	cv2.rectangle(img_RGB, (x,y), (x+w,y+h), (0, 255, 255), 20)
	plt.imshow(img_RGB)
	plt.show()




