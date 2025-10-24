
from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel
from PySide6.QtWidgets import QGridLayout   
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QScreen

from core.UIData import UIData

class ErrorView(QWidget):
    def __init__(self,error_message:str):
        super().__init__()
        ui_data=UIData()
        logo=ui_data.load_svg_icon('logo')

        layout = QGridLayout()
        layout.setAlignment(Qt.AlignCenter)
        
        title_label=QLabel("Oups")
        title_label.setFixedHeight(48)
        error_message_label=QLabel(f"Got Error {error_message}")
        error_message_label.setFixedHeight(48)
        
        layout.addWidget(title_label)
        layout.addWidget(error_message_label)

        self.setLayout(layout)
        window_width,window_height=ui_data.get_usuall_window_sizes()

        self.setWindowIcon(logo)
        self.setFixedSize(window_width,window_height)
        self.setWindowTitle(" ")

        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

