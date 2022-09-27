import sys

from PyQt5.QtWidgets import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtMultimedia import *

class File_load(QDialog):
    def __init__(self):
        super().__init__()
        self.di()

    def di(self):
        self.dir = QFileDialog.getOpenFileName(self, 'select file')
        print(self.dir)

class Main(QWidget):
    def __init__(self):
        super().__init__()

        self.win()

    def win(self):
        self.setGeometry(400, 400, 800, 600)

        self.video_viewer_label = QLabel(self)
        self.video_viewer_label.resize(400, 400)
        self.video_viewer_label.setText('test')

        self.stop_btn = QPushButton(self)
        self.stop_btn.setText('Stop')
        self.stop_btn.resize(100, 100)
        self.stop_btn.clicked.connect(self.stop_click)

        self.show()

    def stop_click(self):
        if self.stop_btn.text() == 'Stop':
            self.stop_btn.setText('Play')
        else:
            self.stop_btn.setText('Stop')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = File_load()
    eb = Main()

    app.exec_()
