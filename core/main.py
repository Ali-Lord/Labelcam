from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

# The starting point of the program
def program():
    app = QApplication([])

    window = QWidget()
    layout = QVBoxLayout()

    photos_btn = QPushButton('Label photos')
    videos_btn = QPushButton('Label videos')
    layout.addWidget(photos_btn)
    layout.addWidget(videos_btn)

    # On click event
    photos_btn.clicked.connect(on_photos_clicked)
    videos_btn.clicked.connect(on_videos_clicked)

    window.setLayout(layout)
    window.show()
    app.exec_()

def on_photos_clicked():
    # TODO: return photos state & log
    print('"Label photos" clicked.')
    return

def on_videos_clicked():
    # TODO: return videos state & log
    print('"Label videos" clicked.')
    return
    
    
program()


