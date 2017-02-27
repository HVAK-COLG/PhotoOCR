import cv2
import numpy as np
from functools import reduce
import math
from PIL import Image, ImageEnhance
from statistics import mean

thresh = 127
contrast = 5.0
sharpness = 1.0
brightness = 1.5


def noise(image):

    kernel = np.ones((2, 2), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image=cv2.dilate(image,kernel,iterations=1)

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

    image = cv2.cvtColor(imageArray, cv2.COLOR_BGR2GRAY)

    img = Image.fromarray(image)

    grayEnhancer = ImageEnhance.Color(img)
    image = grayEnhancer.enhance(0.0)

    imageArray = np.array(imageArray)

    image = cv2.cvtColor(imageArray, cv2.COLOR_BGR2GRAY)

    return image


def binary(img):
    image = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 111, 5)

    (r,c)=img.shape
    for i in range(r):
        for j in range(c):
            if img[i][j] > thresh:
                img[i][j] = 255
            else:
                img[i][j] = 0

    return image