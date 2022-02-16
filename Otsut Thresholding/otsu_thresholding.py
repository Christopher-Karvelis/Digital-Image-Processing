#!/bin/python3 
import sys 
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def thresholding(threshold):
    new_image = []
    #Chhecking if image is RGB and converted to gray
    if(len(image.shape) == 3):
        for i in range(len(image)):
            row = []
            new_image.append(row)
            for j in range(len(image[i])):
                #if image is RGB calculate the average of Red Green Blue values as
                #the new value for every pixel
                new_image[i].append(np.average(image[i][j]))
    else:
        #if its not RGB just copy the image as it is
        new_image = np.copy(image)
        print(new_image)
    #The proccess of the thresholding
    for i in range(len(new_image)):
        for j in range(len(new_image[i])):
            #For each pixel check if its eihter higher than the threshold or lower and set
            #it to the according value
            if(new_image[i][j] > threshold):
                new_image[i][j] = 255
            else:
                new_image[i][j] = 0
    return(new_image)
    #Show image in grayscale with min value(black) = 0 and max value(white) = 255
    #plt.imshow(new_image, cmap="gray", vmin=0, vmax=255)
    #plt.show()
    
#Import image from disk  
image = np.array(Image.open(sys.argv[1]))
threshold = int(sys.argv[3])
#print("-----------ORIGINAL IMAGE-----------")
#Show image in grayscale with min value(black) = 0 and max value(white) = 255
#plt.imshow(image, cmap="gray", vmin=0, vmax=255)
#plt.show()
#Create a new image array that will host the thresholded image
#new_image = np.zeros((image.shape[0],image.shape[1]))
new_image = thresholding(threshold)
#Execute the thresholding proccess for the given threshold value
#print("-----------IMAGE WITH THRESHOLD " + threshold + "-----------")

print(new_image)
#Save the thresholded image to disk
new_image = np.uint8(new_image)
image_array = np.asarray(new_image)
Image.fromarray(image_array).save(sys.argv[2])