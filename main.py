from ctypes import resize
from sklearn.preprocessing import scale
from sympy import im
import cv2
import os

reductPercent = 50
# list all images in the directory
images = []
for root, dirs, files in os.walk('images'):
    for file in files:
        if file.endswith('.jpg') or file.endswith('.png'):
            # print(os.path.join(root, file))
            images.append(os.path.join(root, file))

for image in images:
    img = cv2.imread(image)
    imgWidth = int(img.shape[1])
    imgHeight = int(img.shape[0])
    # if image is more than 500x500, resize it
    if int(img.shape[0]) >= 500 and int(img.shape[1]) >= 500:
        try :
            width = int(imgWidth * reductPercent / 100)
            height = int(img.shape[0] * reductPercent / 100)
            dim = (width, height)
            # resize image
            resizedImg = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
            print(image, "resized from", img.shape, "to", resizedImg.shape)
            # save image
            cv2.imwrite(image, resizedImg)
            print("Image saved")
        except Exception as e:
            print("error : ", e)
    else:
        print("Image is already smaller than 500x500")

print("Done")
