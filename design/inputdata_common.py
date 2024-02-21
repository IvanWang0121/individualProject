from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QMessageBox
import sys
import globals

class PitchShiftingWindow(QWidget):
    def __init__(self):
        super().__init__()


        # 窗口大小
        self.setGeometry(200, 200, 1280, 960)
        self.setFixedWidth(700)
        self.setFixedHeight(400)
        self.setStyleSheet('background-color:white')
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()


        # Label and QLineEdit for second input
        label1 = QLabel("n_steps:", self)
        layout.addWidget(label1)

        self.input1 = QLineEdit(self)
        layout.addWidget(self.input1)

        # Button to confirm and record the numbers
        confirm_button = QPushButton("Confirm", self)
        confirm_button.clicked.connect(self.on_confirm)
        confirm_button.clicked.connect(self.window_after_choosevalue)
        layout.addWidget(confirm_button)

        self.setLayout(layout)

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