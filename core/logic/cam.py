'''
Original author: Ali Raz (Mohammad Saif Ali)
Created: 22.02.2020
Last modified: 06.03.2020

This code is licenced under MIT Licence.

Description:
    A camera class that returns frame, captures photos and captures videos.
'''

import cv2 # Version 4.2.0
import os

# TODO: logging [What the variable and arguments holds, ..etc]
# TODO: in setup.py
import sys
sys.path.append(os.getcwd()[:-6])

from common.data_format_enum import DataFormat

class Camera():
    def __init__(self, cam_index, data_format):
        self.cam_index = cam_index # Which camera? If you have only one camera, this should be -1.

        # Type check
        if type(data_format) is DataFormat:
            self.data_format = data_format # Photo or video? This must be enum where 1 is photo and 2 is video.
        else:
            print("data_format type error in __init__ of Camera class!")
            exit()

        self.capture = cv2.VideoCapture(cam_index)

    # Run this method in a loop if preview is desired. Show the frame with your preferred GUI toolkit.
    # NOTE: Don't forget to run end_process() if you're gonna stop previewing.
    def frame(self):
        read_success, frame = self.capture.read()

        if read_success:
            return True, frame
        else:
            return False, "Unable to read. The method frame() failed."

    # When you no longer require to run the camera class, run this method.
    def end_process(self):
        # TODO: Check if the capture is released or not first.
        self.capture.release()

    def capture_photo(self, save_path, filename):
        success, save_frame = self.frame()

        if success:
            cv2.imwrite(os.path.join(save_path, filename) , save_frame)
            return True
        else:
            #return failed message
            #"Error: Failed to read the image."
            return False
    
    def capture_video_initiate(self, save_path, filename):
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        # ISSUE: FPS is not matching the webcam FPS so the video becomes too fast.
        self.out = cv2.VideoWriter(os.path.join(save_path, filename), fourcc, 24.0, (640, 480))

    def capture_video_begin(self, frame):
        if self.capture.isOpened():           
            print("Saving frame..")
            self.out.write(frame)
    
    def capture_video_end(self):
        self.out.release()
