
from __globals import CACH_REPOSITORY,API_REPOSITORY
from core.EventObserver import EventObserver
from core.Events.ControllerShowViewEvent import ControllerShowViewEvent

# from core.IEventObserverSubscriable import IEventObserverSubscriable

# class Controller(object):
# class Controller(object,IEventObserverSubscriable):
class Controller(object):
    def __init__(self):
        self._window=None
        self._cache_repository=CACH_REPOSITORY
        self._api_repository=API_REPOSITORY
        self._event_observer=EventObserver()
        self.__is_active=True

    def handle_event(self,event)->None:
        print('Dot event shouwing view')
        if type(event)==ControllerShowViewEvent:
            #TODO here
            self._window.show()
            pass
        #handle make it active
        #handle make it inactive
        #handle show event


        pass

    def make_active(self)->None:
        self.__is_active=True
        self._window.setEnabled(True)

    def make_inactive(self)->None:
        self.__is_active=False
        self._window.setEnabled(False)

    def show(self)->None:
        self._window.show()