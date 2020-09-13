import os
import numpy as np
import cv2
import itertools
import glob

source = "reside_dataset/trans/"
destination = "reside_dataset/reside/trans/"
count = 0
base = 1
for img1 in glob.glob(source + "*.png"):
    # print(img1)
    im1 = cv2.imread(img1)
    width = int(im1.shape[1] * (256/620) )
    height = int(im1.shape[0] * (256/460) )
    dim = (width, height)
    img_resized = cv2.resize(im1, dim, interpolation = cv2.INTER_AREA)
    #img_flipped = cv2.flip(im1,1)
    cv2.imwrite(destination + str(base).zfill(5) + "_" +str(1+count%10) + ".png", img_resized )
    count = count+1
    if(count%10==0):
        base = base+1