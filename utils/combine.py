import os
import numpy as np
import cv2
import itertools
import glob
import natsort

source1 = "./reside_dataset/reside_pix2pix/temp/"
source2 = "./reside_dataset/reside_pix2pix/temp1/"
destination = "./reside_dataset/reside_pix2pix/train/"

list1 = os.listdir(source1)
list2 = os.listdir(source2)
list1 = natsort.natsorted(list1,reverse=True)
list2 = natsort.natsorted(list2,reverse=True)
# for (i,j) in zip(list1,list2):
#     print(i,j)

count = 1399
for (img1,img2) in zip(list1,list2):
    im1 = cv2.imread(source1 + img1)
    im2 = cv2.imread(source2 + img2)
    
    
    width = int(im1.shape[1] * (256/620) )
    height = int(im1.shape[0] * (256/460) )
    dim = (width, height)
    img_resized_1 = cv2.resize(im1, dim, interpolation = cv2.INTER_AREA)
    img_resized_2 = cv2.resize(im2, dim, interpolation = cv2.INTER_AREA)

    img_con_h = cv2.hconcat([img_resized_1, img_resized_2])
    cv2.imwrite(destination + str(count).zfill(6) + ".png", img_con_h )
    count = count+1