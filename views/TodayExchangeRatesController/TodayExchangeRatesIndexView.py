
from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel


class TodayExchanegRatesIndexView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Works"))

        self.setLayout(layout)

        self.setFixedSize(768,640)
        self.setWindowTitle(" ")
