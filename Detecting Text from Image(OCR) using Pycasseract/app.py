#importing the libraries

import cv2
import pytesseract as ps
import sys

# Need to initialize the path where your tesseract.exe is found

ps.pytesseract.tesseract_cmd='C:\Program Files\Tesseract-OCR\\tesseract.exe'

#getting image path in cmd

path=sys.argv[1]

#read the image

img=cv2.imread(path)

#convert from bgr to rgb

img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#detect the text in the image

text=ps.image_to_string(img)

#print the text

print(text)