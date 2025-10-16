
import sys

from PySide6.QtWidgets import QApplication
from controllers.TodayExchangeRatesController import TodayExchangeRatesController


def main()->None:
    app=QApplication(sys.argv)
    # TodayExchangeRatesController().index()
    home_controller=TodayExchangeRatesController()

    home_controller.index()

    home_controller.window.show()
    # sys.exit(app.exec())
    app.exec()


if __name__ == "__main__":
    main()