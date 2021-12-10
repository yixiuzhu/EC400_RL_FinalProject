import glob as glob
import cv2
import numpy as np
#import scipy
#import os
import shutil
import skimage.measure
#from pycnn import PyCNN
from skimage import color
#from skimage import io
import time

## Create processed_data folder (Only need to run once!)
origional_folder = r"C:/Users/ericy/OneDrive/2021FW/400_project/EC400_RL_FinalProject/homework5_for_python_3/homework/drive_data"
processed_data_folder = r"C:/Users/ericy/OneDrive/2021FW/400_project/EC400_RL_FinalProject/homework5_for_python_3/homework/processed_data"
shutil.copytree(origional_folder, processed_data_folder)

## Self implemented RGB to Grey function as matplotlib & openCV don't have built in function?
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

loaded_img = []
for imgname in glob.glob("C:/Users/ericy/OneDrive/2021FW/400_project/EC400_RL_FinalProject/homework5_for_python_3/homework/drive_data/*.png"):
    original= cv2.imread(imgname)

    #loaded_img.append(original)                                                            -- just for debug purpose, don't try it
    #print(np.shape(loaded_img))
    print("original size: ", end='')
    print(original.shape)
    #cv2.imshow('original', original)
    #cv2.waitKey(500)
    
    ## Turn 3-channel RGB to 1-channel grey scale image
    grayscale = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    #grayscale = color.rgb2gray(imgname)
    #print(grayscale.shape)
    
    ## OpenCV Canny Edge detector (Canny edge detector only focuses on local changes and it has no understanding of the content of the image, it has limited accuracy)
    v = np.median(grayscale)
    sigma=0.33        # sigma controls the range of threshold, small sigma gives a tighter threshold, vice versa                                                                    
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edges = cv2.Canny(grayscale,lower,upper) # minVal=100, maxVal=100 (could be tuned later)
    # print(edges.shape)
    
    ## Down sample images
    downsample = skimage.measure.block_reduce(edges, (2,2), np.max)
    print("downsample size: ", end='')
    print(downsample.shape)

    #cv2.imshow('downsample', downsample)
    #cv2.waitKey(50000)

    
    ## Standarize data (scale pixel values to have a zero mean and unit variance)           -- no need as our images are all in same scale
    ## Pixel Normalization (scale pixel values to the range 0-1)                            -- no need as our images are all in same scale
    
    ## PyCNN Edge detection (Will leave aside if Canny could produce promising results)
    #cnn = PyCNN()
    
    ## Change file path from drive_data to processed_data 
    processed_img = downsample
    #imgname = imgname.replace('drive_data', 'processed_data')
    imgname = imgname.replace('\\', '/')
    imgname = "\"" + imgname + "\""
    savename = 'C:/Users/ericy/OneDrive/2021FW/400_project/EC400_RL_FinalProject/homework5_for_python_3/homework/processed_data/'
    filename = imgname [imgname.index('drive_data') + 11 : len(imgname)-1]
    savename = savename + filename
    print(savename)
    cv2.imwrite(savename,processed_img)