from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QAbstractButton, QPushButton, QFileDialog, \
    QStackedWidget
from PyQt6.QtGui import QIcon, QFont
from selectFile import SelectFileWindow

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.file_label = None
        self.select1 = SelectFileWindow()

        # 窗口大小
        self.setGeometry(200, 200, 1280, 960)
        self.setFixedWidth(700)
        self.setFixedHeight(300)
        # 窗口标题
        self.setWindowTitle("Audio Processing Tools")
        # 窗口颜色
        self.setStyleSheet('background-color:#E6E6FA')
        # # 菜单栏
        # self.menuBar().addMenu("File")
        # self.menuBar().addMenu("Help")
        # self.menuBar().addMenu("More")
        self.statusBar().showMessage("Welcome to Audio Processing Tools-design by Yifei Wang")
        # 调用创建按钮
        self.create_button()

        # 模式选择文案2
        label = QLabel("Mode Selection", self)  # 字体文案
        # label.setText("Uplode your file")                                   # 更新字体文案
        label.move(260, 20)  # 文案位置
        label.setFont(QFont("Sanserif", 18))  # 文案字体大小
        label.setStyleSheet('color:black')  # 字体颜色
        label.adjustSize()  # 调整标签的大小以适应文本



    # 创建按钮属性
    def create_button(self):
        # 功能1
        btn1 = QPushButton("Format Conversion", self)  # 按钮文案
        btn1.setGeometry(30, 50, 300, 60)  # 调整按钮位置和大小
        btn1.setFont(QFont("Times", 12, QFont.Weight.ExtraBold))  # 按钮字体文案
        btn1.setStyleSheet("background-color: light grey; color: black;")  # 按钮的背景，文本颜色=
        btn1.clicked.connect(self.open_select_window)  # 跳转

        # 功能2
        btn2 = QPushButton("Audio Speed", self)  # 按钮文案
        btn2.setGeometry(30, 130, 300, 60)  # 调整按钮位置和大小
        btn2.setFont(QFont("Times", 12, QFont.Weight.ExtraBold))  # 按钮字体文案
        btn2.setStyleSheet("background-color: light grey; color: black;")  # 按钮的背景，文本颜色=
        btn2.clicked.connect(self.open_select_window)  # 跳转

        # 功能3
        btn3 = QPushButton("Audio Clip", self)  # 按钮文案
        btn3.setGeometry(350, 50, 300, 60)  # 调整按钮位置和大小
        btn3.setFont(QFont("Times", 12, QFont.Weight.ExtraBold))  # 按钮字体文案
        btn3.setStyleSheet("background-color: light grey; color: black;")  # 按钮的背景，文本颜色=
        btn3.clicked.connect(self.open_select_window)

        # 功能4
        btn4 = QPushButton("Pitch Change", self)  # 按钮文案
        btn4.setGeometry(350, 130, 300, 60)  # 调整按钮位置和大小
        btn4.setFont(QFont("Times", 12, QFont.Weight.ExtraBold))  # 按钮字体文案
        btn4.setStyleSheet("background-color: light grey; color: black;")  # 按钮的背景，文本颜色
        btn4.clicked.connect(self.open_select_window)

    def open_select_window(self):
        self.hide()

        self.select1.show()



# 创建应用和窗口
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())



