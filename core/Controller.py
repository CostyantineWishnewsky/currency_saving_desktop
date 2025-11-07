
from abc import ABC,abstractmethod

from __globals import CACH_REPOSITORY,API_REPOSITORY
from core.EventObserver import EventObserver
from core.Events.Controller.ControllerShowViewEvent import ControllerShowViewEvent
from core.Events.Controller.RunControllerEvent import RunControllerEvent
from core.Events.Controller.MakeControllerInactiveEvent import MakeControllerInactiveEvent
from core.Events.Controller.MakeControllerActiveEvent import MakeControllerActiveEvent

class Controller(ABC):
    def __init__(self,id:int):
        self._id=id
        self._window=None
        self._cache_repository=CACH_REPOSITORY
        self._api_repository=API_REPOSITORY
        self.__is_active=True

    def __del__(self):
        event_observer=EventObserver()

        event_observer.unsubscribe(ControllerShowViewEvent,self)
        event_observer.unsubscribe(MakeControllerActiveEvent,self)
        event_observer.unsubscribe(MakeControllerInactiveEvent,self)
        event_observer.unsubscribe(RunControllerEvent,self)

    def get_event_subscribtion_id(self)->int:
        return self._id

    def handle_event(self,event)->None:
        if isinstance(event,RunControllerEvent):
            self.index()
            event_observer=EventObserver()

            event_observer.notify(ControllerShowViewEvent(self._id))
            return
        elif isinstance(event,ControllerShowViewEvent):
            if self._window == None:
                return
            self._window.show()
            return
        elif isinstance(event,MakeControllerInactiveEvent):
            self.__is_active=False
            if self._window == None:
                return
            self._window.setEnabled(False)
            return
        elif isinstance(event,MakeControllerActiveEvent):
            self.__is_active=True
            if self._window == None:
                return
            self._window.setEnabled(True)
            return
        raise Exception(f"Unhandled Event {event}")

    @abstractmethod
    def index(self):
        pass

    def get_event_subscribtion_id(self)->int:
        return self._id
