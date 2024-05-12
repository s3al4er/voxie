import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
import os
import voxie_lib as vxlib

class VoxieApp(QMainWindow):
    def __init__(self):
        super().__init__()

        loadUi('voxie.ui', self)
        
        self.start.clicked.connect(self.startClicked)
        
    def startClicked(self):
        vxlib.listen_and_recognize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VoxieApp()
    window.show()
    sys.exit(app.exec())
