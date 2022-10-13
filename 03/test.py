# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 14:47:17 2021

@author: roor
"""

import matplotlib.pyplot as plt
import load_images as li
import task1 as t1

images = li.getImages()

filtered_image = t1.apply_my_filter(images['Coins'], t1.average_filter())

plt.figure(1)
plt.subplot(1, 2, 1)
li.imshowGray(images['Pics/Coins.png'])
plt.subplot(1, 2, 2)
li.imshowGray(filtered_image)
