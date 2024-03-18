from PyQt5.QtWidgets import QApplication#, QWidget, QLabel, QPushButton, QFileDialog, QMessageBox
import os
import sys
script_dir = os.path.dirname(__file__)
module_dir = os.path.join(script_dir, "..", "GUIUtils")
sys.path.append(module_dir)
from PDFMerger import PDFMerger
from FileIO import FileIO


class PDFMergerApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.file_io = FileIO("PDF Merger")
        self.file_io.show()
        self.file_io.button.clicked.connect(self.merge_selected_files)

    def merge_selected_files(self):
        if self.file_io.files:
            merger = PDFMerger(self.file_io.files)
            merger.merge_pdfs()
            self.file_io.show_popup("PDFs have been merged successfully!")
            self.app.quit()  # Quit the application after merging

    def run(self):
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    app = PDFMergerApp()
    app.run()
