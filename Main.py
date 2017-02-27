import cv2
import InputCapture
import ImageProcessing
import numpy as np
from PIL import Image
import copy

#img = InputCapture.imgcap()
img=cv2.imread("Sample1.jpg")

inp = np.array(img)
inpDisp=copy.deepcopy(inp)

gray = ImageProcessing.graying(inp)
grayDisp = copy.deepcopy(gray)

binary = ImageProcessing.binary(gray)
binaryDisp = copy.deepcopy(binary)

noise = ImageProcessing.noise(binary)
noiseDisp = copy.deepcopy(noise)

while True:
    cv2.imshow("Options", cv2.imread("options.png"))
    cv2.imshow("Image_RGB", inpDisp)
    cv2.imshow("Image_GRAY", grayDisp)
    cv2.imshow("Noise_Reduced", noiseDisp)
    cv2.imshow("Binary_Image", binaryDisp)
    ch = cv2.waitKey(33)
    if ch == ord('q'):
        break

cv2.destroyAllWindows()
