#Detect faces in video
# from mtcnn import MTCNN
# import cv2

# detector=MTCNN()
# img=cv2.VideoCapture('/home/anushka/Documents/facedetection/2.mp4')
# while (True):
# 	success,image = img.read()
# 	output=detector.detect_faces(image)
# 	print(output)
# 	for i in output:
# 		x,y,Width,height=i['box']
# 		# Blue color in BGR
# 		color = (255, 0, 0)
# 		# Line thickness of 2 px
# 		thickness = 2
#  	 	# Using cv2.rectangle() method
# 		# Draw a rectangle with blue line borders of thickness of 2 px
# 		image = cv2.rectangle(image,(x,y), (x+Width,y+height), color, thickness)
# 	cv2.imshow('detection_image',image)
# 	cv2.waitKey(0)
