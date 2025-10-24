
from __globals import CACH_REPOSITORY,API_REPOSITORY

class Controller(object):
    def __init__(self):
        self._window=None
        self._cache_repository=CACH_REPOSITORY
        self._api_repository=API_REPOSITORY
        self.__is_active=True

    def make_active(self)->None:
        self.__is_active=True
        self._window.setEnabled(True)

    def make_inactive(self)->None:
        self.__is_active=False
        self._window.setEnabled(False)

    def show(self)->None:
        self._window.show()