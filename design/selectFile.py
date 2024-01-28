from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QAbstractButton, QPushButton, QFileDialog, \
    QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QMainWindow, QLabel
# from Mainwindow import MainWindow
# from pitchshifting import PitchShiftingWindow

import sys

class SelectFileWindow(QWidget):
    def __init__(self):
        super().__init__()

        #self.select2 = MainWindow()
        # self.select3 = PitchShiftingWindow()

        # 窗口大小
        self.setGeometry(200, 200, 1280, 960)
        self.setFixedWidth(700)
        self.setFixedHeight(400)
        self.setStyleSheet('background-color:pink')

        layout = QVBoxLayout()

        label = QLabel("Select a file:", self)
        layout.addWidget(label)

        select_file_button = QPushButton("select a file", self)
        select_file_button.clicked.connect(self.open_file_dialog)
        layout.addWidget(select_file_button)

        self.file_label = QLabel("", self)
        layout.addWidget(self.file_label)

        self.setLayout(layout)

        comfirmbutton = QPushButton("Comfirm",self)
        comfirmbutton.setGeometry(450, 260, 200, 60)  # 调整按钮位置和大小
        comfirmbutton.setFont(QFont("Times", 12, QFont.Weight.ExtraBold))  # 按钮字体文案
        comfirmbutton.setStyleSheet("background-color: white; color: black;")  # 按钮的背景，文本颜色=
        comfirmbutton.clicked.connect(self.window_after_selection)

        # comfirmbutton = QPushButton("Back",self)
        # comfirmbutton.setGeometry(5, 6, 60, 20)  # 调整按钮位置和大小
        # comfirmbutton.setFont(QFont("Times", 12, QFont.Weight.ExtraBold))  # 按钮字体文案
        # comfirmbutton.setStyleSheet("background-color: white; color: black;")  # 按钮的背景，文本颜色=
        # comfirmbutton.clicked.connect(self.back_last_window())

    def open_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file_dialog.setNameFilter("WAV Files (*.wav)")

        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            for file_name in selected_files:
                print(f"Selected file: {file_name}")
                self.file_label.setText(f"Selected File: {file_name}")

    def window_after_selection(self):
        if self.file_label.text():
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SelectFileWindow()
    window.show()
    sys.exit(app.exec())