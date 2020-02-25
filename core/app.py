from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtCore import Qt

import enum
import sys

from ui_obj.preview import Preview

# Test
import cv2
#from logic.cam import Camera

class DataFormat(enum.Enum):
    photos = 1
    videos = 2

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        preview = Preview(1)

        self.setWindowTitle("Labelcam - Data type: "
                            + "Photos"
                            + ", Camera index: "
                            + str(preview.get_cam_index())
                            + ".")


        
        #self.resize(pixmap.width(), pixmap.height())
        label = preview.get_preview(self)
        
        self.setCentralWidget(label)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
