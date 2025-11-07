
import sys

from PySide6.QtWidgets import QApplication

from core.patterns.SingletonMeta import SingletonMeta
from core.UIData import UIData


from core.Events.EventObserver.RegisterNewItemEvent import RegisterNewItemEvent


class EventObserver(metaclass=SingletonMeta):
    def __init__(self):
        self._application=QApplication(sys.argv)
        self._event_subscribers={}
        self._names_ids={}
        self._last_event_id=1
        self._is_running=False

    def setup(self)->None:
        palette=self._application.palette()
        ui_data=UIData()
        ui_data.set_pallete(palette)

    def notify(self,event)->None:
        if type(event) in self._event_subscribers.keys():
            self._event_subscribers[type(event)][event.id].handle_event(event)
            return
        raise Exception(f"{event} with type{type (event)} is not in events list")
        

    def subscribe(self,event_type,event_subscriber)->None:
        event_subscriber_id=event_subscriber.get_event_subscribtion_id()
        if event_subscriber_id == None:
            raise Exception("event_subscriber_id is None")
        if event_subscriber_id == int:
            raise Exception("event_subscriber_id should be of type int")


        if event_type not in self._event_subscribers.keys():
            self._event_subscribers[event_type]={event_subscriber_id:event_subscriber}

            return
        self._event_subscribers[event_type][event_subscriber_id]=event_subscriber

    def unsubscribe(self,event_type,event_subscriber)->None:
        if event_type not in self._event_subscribers.keys():
            raise Exception(f"There is no subsribtion of {event_subscriber} on {event_type} event")
        event_subscriber_id=event_subscriber.get_event_subscribtion_id()
        if event_subscriber_id not in self._event_subscribers[event_type].keys():
            raise Exception(f"There is no subscriber with id {event_subscriber_id} for {event_type}")
        self._event_subscribers[event_type][event_subscriber_id]=event_subscriber
        
        if event_type not in self._event_subscribers.keys():

            raise Exception("unhandled event")
        if event_subscriber_id not in self._event_subscribers[event_type].keys():
            raise Exception(f"There is no subscriber with id {event_subscriber_id} for {event_type}")
        del self._event_subscribers[event_type][event_subscriber_id]
        
    def get_last_event_subscriber_id(self)->int:
        prev_subscriber_id=self._last_event_id
        self._last_event_id=self._last_event_id+1
        return prev_subscriber_id
    
    def add_subscriber_name(self,name:str,subscriber)->bool:
        if name in self._names_ids.keys():
            return False
        self._names_ids[name]=subscriber

        return True

    def get_id_by_name(self,name:str)->int:
        if name in self._names_ids.keys():
            return self._names_ids[name].get_event_subscribtion_id()
        raise Exception(f"There is no item with name {name}")

    def run(self)->None:
        if self._is_running==True:
            raise Exception("Cannot run application twice")
        self._is_running=True
        self._application.exec()
