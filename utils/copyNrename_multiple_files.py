import os
import numpy as np
import cv2
import itertools
import glob

source = "frida/temp/"
destination = "temp_dataset_cycleGAN/trainB/"
print(source,destination)
count = 198
for img1 in glob.glob(source + "*.png"):
    im1 = cv2.imread(img1)
    #print(img1)
    print(count)
    cv2.imwrite(destination + str(count).zfill(6) + ".png", im1 )
    count = count+1