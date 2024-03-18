import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog, QMessageBox

class FileIO(QWidget):
    def __init__(self, window_title):
        super().__init__()
        self.window_title = window_title
        self.initUI()
        self.files = []

    def initUI(self):
        self.setWindowTitle(self.window_title)

        self.label = QLabel('Select files', self)
        self.label.move(20, 20)

        self.button = QPushButton('Open', self)
        self.button.clicked.connect(self.open_files)
        self.button.move(20, 50)

        self.setGeometry(100, 100, 300, 100)

    def open_files(self):
        # The Native File Dialog in Windows sorts the selected files alphabetically, using QT file dialog to preserve selection order
        files, _ = QFileDialog.getOpenFileNames(self, 'Select files', "", "PDF Files (*.pdf)", options=QFileDialog.DontUseNativeDialog)
        if files:
            for file in files:
                self.files.append(file)

    def show_popup(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        msg.setText(message)
        msg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileIO("FileIO")
    window.show()
    sys.exit(app.exec_())

