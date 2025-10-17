


class Controller(object):
    def __init__(self):
        self._window=None
        self.__is_active=True

    def make_active(self)->None:
        self.__is_active=True
        self._window.setEnabled(True)

    def make_inactive(self)->None:
        self.__is_active=False
        self._window.setEnabled(False)

    def show(self)->None:
        self._window.show()