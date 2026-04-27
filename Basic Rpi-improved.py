from picamera2 import Picamera2
import matplotlib.pyplot as plt #import matplotlib
import cv2 #import OpenCV
import time

# Initialize camera
picam2 = Picamera2()

# Configure camera
picam2.configure(picam2.create_preview_configuration())

# Start camera
picam2.start()

# Allow camera warm-up
time.sleep(2)

# Capture image
image = picam2.capture_array()

# Convert BGR to RGB for matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Show image
plt.imshow(image_rgb)
plt.title("Captured Image")
plt.axis('off')
plt.show()

# Stop camera
picam2.stop()