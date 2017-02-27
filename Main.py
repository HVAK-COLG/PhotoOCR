import cv2
import InputCapture
import ImageProcessing
import numpy as np
from PIL import Image

img = InputCapture.imgcap()
input = np.array(img)

gray = ImageProcessing.graying(input)
noise = ImageProcessing.noise(gray)
binary = ImageProcessing.binary(noise)

while True:
    cv2.imshow("Image_RGB", input)
    cv2.imshow("Image_GRAY", gray)
    cv2.imshow("Noise_Reduced", noise)
    cv2.imshow("Binary_Image", binary)
    ch = cv2.waitKey(33)
    if ch == ord('q'):
        break

cv2.destroyAllWindows()
