
from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel

from core.UIData import UIData

class ErrorView(QWidget):
    def __init__(self,error_message:str):
        super().__init__()
        ui_data=UIData()


        

        layout = QVBoxLayout()

        title_label=QLabel("Oups")
        error_message_label=QLabel(f"Got Error {error_message}")
        # layout.addWidget(QLabel(f"Got Error {error_message}"))

        layout.addWidget(title_label)
        layout.addWidget(error_message_label)

        self.setLayout(layout)
        window_width,window_height=ui_data.get_usuall_window_sizes()
        self.setFixedSize(window_width,window_height)
