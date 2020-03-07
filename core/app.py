from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtCore import Qt

import enum
import sys

from ui_obj.preview import Preview

class DataFormat(enum.Enum):
    photos = 1
    videos = 2

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.bPreview = True;
        self.preview = Preview(1)

        self.setWindowTitle("Labelcam - Data type: "
                            + "Photos"
                            + ", Camera index: "
                            + str(self.preview.get_cam_index())
                            + ".")

        self.label = self.preview.set_preview(self)

        self.setCentralWidget(self.label)

    # Overriding the closeEvent method
    def closeEvent(self, event):
        self.bPreview = False
        self.preview.stop_preview()
        event.accept()
        exit()

    def refresh_preview(self):
        while (self.bPreview):
            self.label.setAlignment(Qt.AlignCenter)
            self.label.setPixmap(self.preview.refresh_preview())
            QApplication.processEvents()


app = QApplication(sys.argv)

window = MainWindow()
window.show()
window.refresh_preview()

app.exec_()
