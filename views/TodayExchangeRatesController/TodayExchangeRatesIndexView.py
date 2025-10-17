
from PySide6.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout,QLabel
from PySide6.QtWidgets import QScrollArea

from PySide6.QtCore import Qt

from core.UIData import UIData

from models.ExchangeRate import ExchangeRate


class TodayExchanegRatesIndexView(QWidget):
    def __init__(self,exchange_rates:list[ExchangeRate]):
        super().__init__()
        self._exchange_rates=exchange_rates

        ui_data=UIData()

        layout = QVBoxLayout()

        #Main
        main_wrapper=QWidget()
        main=QHBoxLayout(main_wrapper)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True) 
        
        content = QWidget()
        content_layout = QVBoxLayout(content)

        #Here should be adding exchange_rates
        for i in range(10):
            label = QLabel(f"Label #{i+1}")
            content_layout.addWidget(label)

        # Add content into scroll area
        scroll.setWidget(content)
        main.addWidget(scroll)


        #Footer
        footer_wrapper=QWidget()
        footer_wrapper.setStyleSheet(f"background-color: {ui_data.get_base_color().name()};padding: 0rem 0rem;color:{ui_data.get_text_color().name()};")
        footer_wrapper.setFixedHeight(48)

        footer=QHBoxLayout(footer_wrapper)
        footer.addWidget(QLabel("Footer"),alignment=Qt.AlignHCenter)
        
        
        layout.addWidget(main_wrapper)
        layout.addWidget(footer_wrapper)


        self.setLayout(layout)

        window_width,window_height=ui_data.get_usuall_window_sizes()
        self.setFixedSize(window_width,window_height)
        self.setWindowTitle(" ")
