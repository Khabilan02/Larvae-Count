# 1. Threshold
# 2. Resize
# 3. Floodfill

import numpy
import cv2
import time

def first(image):
    diff = (3, 3, 3)
    #mask = numpy.zeros((h + 2, w + 2), numpy.uint8)
    #cv2.floodFill(image, mask, (0, 0), (255, 255, 255), diff, diff)

    return


def main():

    fname = 'C:/Users/User/Desktop/SDP-PROJECT/samples/17.jpg'
    image = cv2.imread(fname)

    #print(image)

    height, width = image.shape[:2]
    diff = (9,9,9)
    mask = numpy.zeros((height+2, width+2), numpy.uint8)


    T, I = cv2.threshold(I, 180, 255, cv2.THRESH_BINARY)


    cv2.imshow("floodfill.png", image) # Save image
    cv2.waitKey(10000)  # Display the image for a short time

    #print(image)
    #cv2.imshow('image', image)
    #cv2.waitKey(5)
    #time.sleep(5)


    return

if __name__  == "__main__":
    main()