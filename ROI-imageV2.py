import numpy as np
from PIL import Image

#1.Open oriinal JPG
img =  Image.open('image2.jpg')
img_array = np.array(img)

#2.Manually adjust the numbers:
#[y_top:y_bottom, x_left:x_right]
y_top = 100 #y1
y_bottom = 2500 #y2
x_left = 150 #x1
x_right = 1500 #x2

roi_array = img_array[y_top:y_bottom, x_left:x_right]

#3.Convert back and save
roi = Image.fromarray(roi_array)
roi.save('my_manual_crop.jpg')
roi.show()