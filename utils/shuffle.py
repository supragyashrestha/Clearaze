import os
import numpy as np
import cv2
import itertools
import glob
import random

source = "./reside_dataset/reside_pix2pix/train/"
destination = "./reside_dataset/reside_pix2pix/temp/"
list1 = os.listdir(source)
#print(list1)
random.shuffle(list1)
#print(list1)
count = 0
for img1 in list1:
    # print(img1)
    im1 = cv2.imread(source + img1)
    cv2.imwrite(destination + str(count).zfill(5) + ".png", im1 )
    count = count+1