


class Controller(object):
    def __init__(self):
        self._window=None
        self.__is_active=True

    def make_active(self)->None:
        self.__is_active=True
        #Make View Active

    def make_inactive(self)->None:
        self.__is_active=False
        #Make View Not Active

    def show(self)->None:
        self._window.show()