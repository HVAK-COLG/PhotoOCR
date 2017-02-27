import cv2
import InputCapture
import ImageProcessing
import numpy as np
from PIL import Image
import copy

# img = InputCapture.imgcap()
img = Image.open("Sample1.jpg")
w, h = img.size
ar = w / h
print(ar)
if ar > 1:
    img = img.resize((1080, (int)(1080 / ar)), Image.ANTIALIAS)
else:
    img = img.resize(((int)(1080 * ar), 1080), Image.ANTIALIAS)

inp = np.array(img)
imgDisp = copy.deepcopy(inp)
orig = copy.deepcopy(inp)

gray = ImageProcessing.graying(inp)
grayDisp = copy.deepcopy(gray)

noise = ImageProcessing.noise(gray)
noiseDisp = copy.deepcopy(noise)

binary = ImageProcessing.binary(gray)
binaryDisp = copy.deepcopy(binary)

inv = ImageProcessing.invert(binary)
invDisp = copy.deepcopy(inv)

contours = ImageProcessing.textarea(inv)

cv2.imshow("INV_Binary_Image", inv)

# to display bounding box around text in image
for contour in contours:
    # edges of bounding box
    [x, y, w, h] = cv2.boundingRect(contour)

    # Avoiding false trues , lesser than 50x50 size
    if w < 100 and h < 100:
        continue

    # drawing bounding box on original input image
    cv2.rectangle(imgDisp, (x, y), (x + w, y + h), (255, 0, 255), 2)

cv2.imshow("Detected", imgDisp)

while True:
    ch = cv2.waitKey(33)
    if ch == ord('q'):
        break

cv2.destroyAllWindows()
