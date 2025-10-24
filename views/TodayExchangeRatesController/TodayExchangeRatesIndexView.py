
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

        counter=0
        line_wrapper=QWidget()
        line=QHBoxLayout(line_wrapper)
        for i in range(len(self._exchange_rates)):
            card_wrapper=QWidget()
            card=QVBoxLayout(card_wrapper)
            #Here should be styling
            currencies_label=QLabel(f"{self._exchange_rates[i].currency_from.name}->{self._exchange_rates[i].currency_to.name}")
            value_label=QLabel(f"{self._exchange_rates[i].value}")
            source_of_information_label=QLabel(f"{self._exchange_rates[i].source_of_information.name}")

            card.addWidget(currencies_label)
            card.addWidget(value_label)
            card.addWidget(source_of_information_label)

            line.addWidget(card_wrapper)
            if counter==2:
                # content_layout.addWidget(card_wrapper)
                content_layout.addWidget(line_wrapper)
                counter=0
                line_wrapper=QWidget()
                line=QHBoxLayout(line_wrapper)
                continue
            counter+=1

        # Add content into scroll area
        scroll.setWidget(content)
        main.addWidget(scroll)


        #Footer
        footer_wrapper=QWidget()
        footer_wrapper.setStyleSheet(f"background-color: {ui_data.get_base_color().name()};padding: 0rem 0rem;color:{ui_data.get_text_color().name()};")
        footer_wrapper.setFixedHeight(48)

        footer=QHBoxLayout(footer_wrapper)
        footer.addWidget(QLabel("Author:Costyantine Wishnewsky"),alignment=Qt.AlignHCenter)
        
        
        layout.addWidget(main_wrapper)
        layout.addWidget(footer_wrapper)


        self.setLayout(layout)

        window_width,window_height=ui_data.get_usuall_window_sizes()
        self.setFixedSize(window_width,window_height)
        self.setWindowTitle(" ")
