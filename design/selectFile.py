from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QAbstractButton, QPushButton, QFileDialog, \
    QVBoxLayout, QMessageBox
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QMainWindow, QLabel


import sys
import globals
from design.inputdata_common import PitchShiftingWindow


class SelectFileWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.select2 = PitchShiftingWindow()

        # 窗口大小
        self.setGeometry(200, 200, 1280, 960)
        self.setFixedWidth(700)
        self.setFixedHeight(300)
        self.setStyleSheet('background-color:#E6E6FA')
        self.setWindowTitle("Audio Processing Tools")

        layout = QVBoxLayout()

        label = QLabel("Choose your ideal file\n   ('.mp3'&'.wav'):", self)
        layout.addWidget(label)

        select_file_button = QPushButton("select a file", self)
        select_file_button.setStyleSheet("background-color: light grey; color: black;")  # 按钮的背景，文本颜色=
        select_file_button.clicked.connect(self.open_file_dialog)
        layout.addWidget(select_file_button)

        self.file_label = QLabel("", self)
        layout.addWidget(self.file_label)

        self.setLayout(layout)

        comfirmbutton = QPushButton("Comfirm",self)
        comfirmbutton.setGeometry(450, 190, 200, 60)  # 调整按钮位置和大小
        comfirmbutton.setFont(QFont("Times", 12, QFont.Weight.ExtraBold))  # 按钮字体文案
        comfirmbutton.setStyleSheet("background-color: light grey; color: black;")  # 按钮的背景，文本颜色=
        comfirmbutton.clicked.connect(self.window_after_selection)


    def open_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file_dialog.setNameFilter("Audio Files (*.wav *.mp3)")

        if file_dialog.exec():
            globals.selected_files = file_dialog.selectedFiles()

            selected_files = file_dialog.selectedFiles()
            for file_name in selected_files:
                print(f"Selected file: {file_name}")
                self.file_label.setText(f"Selected File: {file_name}")

    def window_after_selection(self):
        if globals.selected_files:
            self.hide()
            self.select2.show()
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setText("No file selected")
            msgBox.setInformativeText("Please select a file before confirming.")
            msgBox.setWindowTitle("Warning")
            msgBox.exec()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SelectFileWindow()
    window.show()
    sys.exit(app.exec())