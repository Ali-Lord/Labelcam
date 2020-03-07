'''
Original author: Ali Raz (Mohammad Saif Ali)
Created: 22.02.2020
Last modified: 08.03.2020

This code is licenced under MIT Licence.

Description:
    A camera class that returns frame, captures photos and captures videos.
'''

import cv2 # Version 4.2.0
import os
import logging
logging.info("cam.py loaded.")

class Camera():
    def __init__(self, cam_index):
        self.cam_index = cam_index # Which camera? If you have only one camera, this should be -1.       
        self.capture = cv2.VideoCapture(cam_index)
        logging.info("Camera index is %s. [__init__() from Camera() in cam.py]", str(cam_index))

    # Run this method in a loop if preview is desired. Show the frame with your preferred GUI toolkit.
    # NOTE: Don't forget to run end_process() if you're gonna stop previewing.
    def frame(self):
        read_success, frame = self.capture.read()

        if read_success:
            return True, frame
        else:
            logging.error("Unable to read an image. [frame() from Camera() in cam.py]")
            return False

    # When you no longer require to run the camera class, run this method.
    def end_process(self):
        logging.info("Releasing.. [end_process() from Camera() in cam.py]")
        self.capture.release()
        logging.info("Released. [end_process() from Camera() in cam.py]")

    def capture_photo(self, save_path, filename):
        success, save_frame = self.frame()
        
        save_path = os.path.join(save_path, filename)
        logging.info("The save path is: %s [capture_photo() from Camera() in cam.py]", save_path)

        if success:
            cv2.imwrite(save_path, save_frame)
            return True
        else:
            logging.error("self.frame() returned false. [capture_photo() from Camera() in cam.py]")
            return False
    
    def capture_video_initiate(self, save_path, filename):
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        # ISSUE: FPS is not matching the webcam FPS so the video becomes too fast.
        fps = 24.0
        resolution = (640, 480)
        save_path = os.path.join(save_path, filename)
        self.out = cv2.VideoWriter(save_path, fourcc, fps, resolution)
        logging.info("The save path is: %s [capture_video_initiate() from Camera() in cam.py]", save_path)

    def capture_video_begin(self, frame):
        if self.capture.isOpened():
            self.out.write(frame)
        else:
            logging.error("Capture is closed. [capture_video_begin() from Camera() in cam.py]")

    
    def capture_video_end(self):
        logging.info("Releasing.. [capture_video_end() from Camera() in cam.py]")
        self.out.release()
        logging.info("Released. [capture_video_end() from Camera() in cam.py]")

