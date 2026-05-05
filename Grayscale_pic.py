from PIL import Image

#1.Open the JPG image
img = Image.open('image.jpg')

#2.convert to Grayscale
gray_img = img.convert('L')

#3.Save the result
gray_img.save('gray_picture.jpg')

#4.Show the image
gray_img.show()