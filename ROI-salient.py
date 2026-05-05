import numpy as np
from PIL import Image, ImageFilter

#1.Load captured image
img = Image.open('image2.jpg').convert('L')#Convert to grayscale

#2.Apply a light blur and a heavy blur
light_blur = img.filter(ImageFilter.GaussianBlur(radius=2))
heavy_blur = img.filter(ImageFilter.GaussianBlur(radius=10))

#3.Use NumPy to calculate the difference (the 'Salient Map')
arr_light = np.array(light_blur, dtype=float)
arr_heavy = np.array(heavy_blur, dtype=float)

#Subtract and take absolute  value to find salient regions
salient_map_arr = np.abs(arr_light - arr_heavy)

#4.Normalize and convert back to image
salient_map_arr = (salient_map_arr / salient_map_arr.max()) * 255
salient_map = Image.fromarray(salient_map_arr,astype('uint8'))

#5.Show results
salient_map.show()
salient_map,save('saliency_output.jpg')