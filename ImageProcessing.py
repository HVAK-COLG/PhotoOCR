import cv2
import numpy as np
from PIL import Image, ImageEnhance

thresh = 127
contrast = 5.0
sharpness = 1.0
brightness = 1.5


def noise(image):
    img_bw = 255 * (image > 5).astype('uint8')
    se1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    se2 = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    mask = cv2.morphologyEx(img_bw, cv2.MORPH_CLOSE, se1)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, se2)

    out = image * mask

    return out


def invert(image):
    image = 255 - image
    return image


def graying(image):
    img = Image.fromarray(image)

    grayEnhancer = ImageEnhance.Brightness(img)
    imageArray = grayEnhancer.enhance(brightness)

    grayEnhancer = ImageEnhance.Contrast(imageArray)
    imageArray = grayEnhancer.enhance(contrast)

    grayEnhancer = ImageEnhance.Sharpness(imageArray)
    imageArray = grayEnhancer.enhance(sharpness)

    imageArray = np.array(imageArray)

    image = cv2.cvtColor(imageArray, cv2.COLOR_BGR2YUV)

    img = Image.fromarray(image)

    # grayEnhancer = ImageEnhance.Color(img)
    # image = grayEnhancer.enhance(0.0)

    imageArray = np.array(imageArray)

    image = cv2.cvtColor(imageArray, cv2.COLOR_BGR2GRAY)

    return image


def binary(img):
    image = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 151, 10)
    return image


def textarea(image):
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    dilated = cv2.dilate(image, kernel, iterations=8)
    img, contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return contours
