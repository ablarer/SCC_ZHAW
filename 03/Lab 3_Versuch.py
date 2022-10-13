import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

from PIL import Image
import PIL

import cv2


file_name = ['Pics_Versuch/mignon.jpg', 'Pics_Versuch/sunflowers.jpg']
for file_name in file_name:
    picture = cv2.imread(file_name)
    plt.figure(figsize=(10,10))
    plt.imshow(cv2.cvtColor(picture, cv2.COLOR_BGR2RGB))
    plt.title(file_name)
    plt.show()

# ----------------------------------------------------- load cell image ------------------------------------------------------------------------------
# Summarize some details about the image
def get_image_array(file_name, print_info=True):
    image = Image.open(file_name)
    image_gray = np.array(image)
    if print_info:
        print("Filename:", image.filename)
        print("File format:", image.format)
        print("Shape:", image_gray.shape)
        print('Numpy array dtype:', image_gray.dtype)
        print()

    return image


# https://www.geeksforgeeks.org/image-processing-in-python-scaling-rotating-shifting-and-edge-detection/
file_name = ['Pics_Versuch/mignon.jpg', 'Pics_Versuch/sunflowers.jpg']
for file_name in file_name:
    picture = cv2.imread(file_name)
    # Get number of pixel horizontally and vertically.
    (height, width) = picture.shape[:2]
    print('Heigth: ', height, 'Width ', width)
    filename = file_name.split('/')
    print("Filename:", filename[1])

    # Specify the size of image along with interpolation methods.
    # cv2.INTER_AREA is used for shrinking
    # cv2.INTER_CUBIC is used for zooming.
    result = cv2.resize(picture, (int(width / 2), int(height / 2)), interpolation = cv2.INTER_CUBIC)

    # Write image back to disk.
    image_path_and_name = 'Results/' + filename[1]
    print(image_path_and_name)
    cv2.imwrite(image_path_and_name, result)

# for file_name in file_name:
#    get_image_array(file_name)