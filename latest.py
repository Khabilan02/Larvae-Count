import cv2
import numpy
import time
import threading
#import BlynkLib
from blynklib import Blynk
import time

# Initialize the Blynk library with your authentication token.
BLYNK_AUTH_TOKEN = 'RjVlf4rWlwJyJP7yk8e6UgNWInzVIQwz'
blynk = Blynk(BLYNK_AUTH_TOKEN, server="blynk.cloud")

def image_processing():
    # Select camera
    # 0: First camera / Laptop webcam
    # 1: USB
    # In rasp pi use 0

    camera_index = 1


    cam = cv2.VideoCapture(camera_index)
    time.sleep(0.2)
    

    while True:
        success, image = cam.read()
        #print(image.shape)
        #cv2.imshow('Input Image', image[:,:, 0])
        #cv2.imshow('Input Image', image[:,:, 1])

        # Logicool C270p (640, 480, 3)


        image_height, image_width, depth = image.shape
        scale = 2 # Smaller
        #print(image_height//scale, image_width)

        resized_image = cv2.resize(image, (int(image_width/scale), int(image_height/scale)))

        cv2.imshow('Input Image', resized_image)


        #cv2.imshow('Processed Image', I)
        cv2.waitKey(5)  # Display the image for a short time
        #time.sleep(2)
    cam.release()
    cv2.destroyAllWindows()
    return

    while True:
        success, image = cam.read()



        I = image  # No need to resize
        # I = cv2.imread('7.jpg')
        I = cv2.resize(I, (500, 500))
        cv2.imshow('Input Image', I)


        h, w = I.shape[:2]
        diff = (3, 3, 3)
        mask = numpy.zeros((h + 2, w + 2), numpy.uint8)
        cv2.floodFill(I, mask, (0, 0), (255, 255, 255), diff, diff)

        T, I = cv2.threshold(I, 180, 255, cv2.THRESH_BINARY)

        I = cv2.medianBlur(I, 19)

        totalseeds = 0
        oldlinecount = 0

        for y in range(h):
            linecount = 0
            start = 0
            inside_line = False

            for x in range(w):
                c = numpy.all(I[y, x] < 128)

                if c:
                    if not inside_line:
                        start = x
                        inside_line = True
                else:
                    if inside_line and (x - start) > 10:
                        linecount += 1
                        inside_line = False

            if oldlinecount > linecount:
                totalseeds += oldlinecount - linecount
            oldlinecount = linecount

        print('Total Larva:', totalseeds)

        # Send the 'totalseeds' value to Blynk
        blynk.virtual_write(0, totalseeds)  # Change '0' to the appropriate virtual pin number.

        cv2.imshow('Processed Image', I)
        cv2.waitKey(1)  # Display the image for a short time

    cam.release()
    cv2.destroyAllWindows()

# Create a separate thread for image processing
image_processing_thread = threading.Thread(target=image_processing)

if __name__ == '__main__':
    # Start the image processing thread
    image_processing_thread.start()

    # Initialize Blynk
    #while True:
    #    blynk.run()