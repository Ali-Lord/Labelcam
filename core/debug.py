'''
Original author: Ali Raz (Mohammad Saif Ali)
Created: 22.02.2020
Last modified: 06.03.2020

This code is licenced under MIT Licence.

Description:
    All the debugging codes will be here.
'''

# Preview, capture photo and capture video.
from logic.cam import Camera
import cv2
from common.data_format_enum import DataFormat

camera = Camera(-1, DataFormat.photo)

while(True):
    success, preview_frame = camera.frame()
    if success:
        cv2.imshow("Preview", preview_frame)
    else:
        print("Failed!")
        break

    k = cv2.waitKey(33)

    if k==27:
        break
    elif k == ord('p'):
        # Capture photo and save test
        success = camera.capture_photo("/home/ali/Projects/Labelcam/tmp/", "test.jpg")

        if success:
            print("Saved.")
        else:
            print("Failed.")
    elif k == ord('v'):
        #sucess = print("Not yet, honey.")
        camera.capture_video("/home/ali/Projects/Labelcam/tmp/", "test.avi")
        

camera.end_process()
cv2.destroyAllWindows()
