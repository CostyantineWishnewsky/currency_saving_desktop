
from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel

from models.ExchangeRate import ExchangeRate

class TodayExchanegRatesIndexView(QWidget):
    def __init__(self,exchange_rates:list[ExchangeRate]):
        super().__init__()
        self._exchange_rates=exchange_rates


        layout = QVBoxLayout()
        layout.addWidget(QLabel("Works"))

        self.setLayout(layout)

        self.setFixedSize(768,640)
        self.setWindowTitle(" ")
