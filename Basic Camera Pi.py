from picamera2 import Picamera2
import matplotlib.pyplot as plt

# Initialize camera
picam2 = Picamera2()
picam2.start()

# Capture image
image = picam2.capture_array()

# Show image
plt.imshow(image)
plt.title("Captured Image")
plt.axis('off')

#print the image
print(image.shape)

#capture image and save them
import cv2
cv2.imwrite("image1.jpg", image)

#Modify resolution
config = picam2.create_preview_configuration(main={"size": (640, 480)})
picam2.configure(config)
