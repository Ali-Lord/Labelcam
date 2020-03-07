import sys
sys.path.append('../')

from logic.cam import Camera
import cv2

from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt                                                 

class Preview:
    def __init__(self, cam_index):
        self.cam_index = cam_index

    def set_preview(self, QMainWindow):
        self.label = QLabel(QMainWindow)
        
        self.camera = Camera(-1, "photos")
        frame = self.camera.start_preview()

        # Converting numpy.ndarray to QPixmap
        height, width, channel = frame.shape
        bytes_per_line = 3 * width
        processed_frame = QImage(frame.data,
                                 width,
                                 height,
                                 bytes_per_line,
                                 QImage.Format_BGR888)
        pixmap = QPixmap(processed_frame)
        
        self.label.setPixmap(pixmap)
        self.label.setAlignment(Qt.AlignCenter)  
        
        return self.label

    def refresh_preview(self):
        self.camera = Camera(-1, "photos")
        frame = self.camera.start_preview()

        # Converting numpy.ndarray to QPixmap
        height, width, channel = frame.shape
        bytes_per_line = 3 * width
        processed_frame = QImage(frame.data,
                                 width,
                                 height,
                                 bytes_per_line,
                                 QImage.Format_BGR888)
        pixmap = QPixmap(processed_frame)
        
        return pixmap
    
    def set_cam_index(self, cam_index):
        self.cam_index = cam_index

    def get_cam_index(self):
        return self.cam_index

    def stop_preview(self):
        self.camera.stop_preview()

    def init_preview(self):
        self.camera.init_preview()
        
        
    
