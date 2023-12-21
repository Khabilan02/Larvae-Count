import numpy as np
import cv2
import time

def flood_fill(image):
    h, w = image.shape[:2]
    diff = (3, 3, 3)
    mask = np.zeros((h + 2, w + 2), np.uint8)
    cv2.floodFill(image, mask, (0, 0), (255, 255, 255), diff, diff)

def main():
    fname = 'C:/Users/User/Desktop/SDP-PROJECT/samples/32.jpg'
    image = cv2.imread(fname)

    # Perform flood fill operation
    flood_fill(image)

    # Display the image after flood fill
    cv2.imshow("Flood Fill", image)
    cv2.waitKey(0)

    # Apply threshold to the flooded image
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresholded_image = cv2.threshold(gray_image, 180, 255, cv2.THRESH_BINARY)

    # Display the thresholded image
    cv2.imshow("Thresholded Image", thresholded_image)
    cv2.waitKey(0)

    # Apply median blur to the thresholded image
    thresholded_image = cv2.medianBlur(thresholded_image, 19)

    # Display the final result after median blur
    cv2.imshow("Final Result", thresholded_image)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
