import matplotlib.pyplot as plt
import load_images as li
import numpy as np
from scipy import ndimage

images = li.getImages()
plt.imshow(images['Sunflowers'], cmap='gray')
print(images.keys())

def get_intensity(img,i,j):
    if i < 0 or i >= len(img):
        return 0.0
    elif j < 0 or j >= len(img[0]):
        return 0.0
    else:
        return img[i,j]

def apply_filter(img, i, j, F):
    res = np.ones(F.shape)
    for x in range(i-(F.shape[0]-1)//2, i+(F.shape[1]+1)//2):
        for y in range(j-1, j+2):
            res[(x+1)-i,(y+1)-j] = get_intensity(img, x, y)
    res = (res * F).sum()
    return res


def my_filter(img, F):
    img = img.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i,j] = apply_filter(img, i, j, F)
    return img

# Average filter
F = (1/9) * np.ones((3,3))



plt.subplot(1, 3, 1)
img_filtered = my_filter(images['Sunflowers'], F)
plt.imshow(img_filtered, cmap='gray', vmin=0, vmax=1)
plt.title("Manually filtered")

plt.subplot(1, 3, 2)
plt.imshow(images['Sunflowers'], cmap='gray', vmin=0, vmax=1)
plt.title("Original")

plt.subplot(1, 3, 3)
image_lib = ndimage.convolve(images['Sunflowers'], F)
plt.imshow(image_lib, cmap='gray', vmin=0, vmax=1)
plt.title("Filtered by library")

plt.tight_layout()
plt.show()

