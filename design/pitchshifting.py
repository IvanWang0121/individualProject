from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout
import sys

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

        # Label and QLineEdit for first input
        label1 = QLabel("sr:", self)
        layout.addWidget(label1)

        self.input1 = QLineEdit(self)
        layout.addWidget(self.input1)

        # Label and QLineEdit for second input
        label2 = QLabel("n_steps:", self)
        layout.addWidget(label2)

        self.input2 = QLineEdit(self)
        layout.addWidget(self.input2)

        # Button to confirm and record the numbers
        confirm_button = QPushButton("Confirm", self)
        confirm_button.clicked.connect(self.on_confirm)
        layout.addWidget(confirm_button)

        self.setLayout(layout)

    def on_confirm(self):
        value1 = self.input1.text()
        value2 = self.input2.text()

        # Do something with the recorded values
        print(f"Recorded values: {value1}, {value2}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PitchShiftingWindow()
    window.show()
    sys.exit(app.exec())