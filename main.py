import face_detection


import numpy as np
import cv2


file_name="test_images/test.jpg"
cv2.imshow('img',face_detection.Detection_haar(file_name))
cv2.waitKey(0)
cv2.destroyAllWindows()


#print(face_detection.Detection1(1));

