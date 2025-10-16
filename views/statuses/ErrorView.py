
from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel


class ErrorView(QWidget):
    def __init__(self,error_message:str):
        super().__init__()

        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"Got Error {error_message}"))


        self.setLayout(layout)
        self.setFixedSize(768,640)
