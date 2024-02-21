from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QMessageBox
import sys
import globals



class PitchShiftingWindow(QWidget):
    def __init__(self):
        super().__init__()



        # 窗口大小
        self.setGeometry(200, 200, 1280, 960)
        self.setFixedWidth(700)
        self.setFixedHeight(300)
        self.setStyleSheet('background-color:#E6E6FA')
        self.setWindowTitle("Audio Processing Tools")


        # Label and QLineEdit for second input
        label1 = QLabel("Please input your ideal value for\nn_steps:", self)
        label1.move(10, 10)  # 移动到窗口中的(10, 10)位置
        label1.resize(200, 40)  # 设置标签的宽度和高度


        confirm_button = QPushButton("Confirm", self)
        confirm_button.setGeometry(450, 190, 200, 60)  # 调整按钮位置和大小
        confirm_button.setFont(QFont("Times", 12, QFont.Weight.ExtraBold))  # 按钮字体文案
        confirm_button.setStyleSheet("background-color: light grey; color: black;")  # 按钮的背景，文本颜色=
        confirm_button.clicked.connect(self.on_confirm)
        confirm_button.clicked.connect(self.window_after_choosevalue)


        self.input1 = QLineEdit(self)
        self.input1.move(10, 50)  # 移动到窗口中的(10, 60)位置
        self.input1.resize(200, 30)  # 设置输入框的宽度和高度
        self.input1.setStyleSheet("background-color: #FFFFF0; color: black;")  # 按钮的背景，文本颜色=

    def on_confirm(self):

        value1 = self.input1.text()

        globals.n_steps_value_common = value1

    def window_after_choosevalue(self):
        if globals.n_steps_value_common:
            self.hide()
            self.select2.show()
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setText("No value")
            msgBox.setInformativeText("Please enter n_steps before confirming.")
            msgBox.setWindowTitle("Warning")
            msgBox.exec()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PitchShiftingWindow()
    window.show()
    sys.exit(app.exec())