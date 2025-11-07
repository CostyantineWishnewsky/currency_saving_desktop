

from core.patterns.SingletonMeta import SingletonMeta
from core.EventObserver import EventObserver

from core.Events.ControllerCreator.CreateHomeControllerEvent import CreateHomeControllerEvent
from core.Events.ControllerCreator.GotErrorEvent import GotErrorEvent
from core.Events.ControllerCreator.ShowErrorEvent import ShowErrorEvent

from core.Events.Controller.RunControllerEvent import RunControllerEvent
from core.Events.Controller.ControllerShowViewEvent import ControllerShowViewEvent
from core.Events.Controller.MakeControllerActiveEvent import MakeControllerActiveEvent
from core.Events.Controller.MakeControllerInactiveEvent import MakeControllerInactiveEvent

from controllers.TodayExchangeRatesController import create_TodayExchangeRatesController_data, TodayExchangeRatesController

from controllers.ErrorController import create_ErrorController_data,ErrorController

class ControllersCreator(metaclass=SingletonMeta):
    def __init__(self,id:int) -> None:
        self._event_subscribtion_id=id


    def setup(self)->None:
        event_observer=EventObserver()
    
        event_observer.subscribe(CreateHomeControllerEvent,self)
        event_observer.subscribe(GotErrorEvent,self)

        event_observer.add_subscriber_name('error_handling',self)
    
    def handle_event(self,event)->None:
        event_observer=EventObserver()
        if isinstance(event,CreateHomeControllerEvent): 
            new_id=event_observer.get_last_event_subscriber_id()

            data=create_TodayExchangeRatesController_data(new_id)
            controller=TodayExchangeRatesController(data)
            event_observer.subscribe(RunControllerEvent,controller)
            event_observer.subscribe(ControllerShowViewEvent,controller)
            event_observer.subscribe(MakeControllerInactiveEvent,controller)
            event_observer.subscribe(MakeControllerActiveEvent,controller)

            event_observer.add_subscriber_name('home',controller)
            return
        elif isinstance(event,GotErrorEvent):
            new_id=event_observer.get_last_event_subscriber_id()
            
            data=create_ErrorController_data(new_id,event.error_message)
            controller=ErrorController(data)

            
            event_observer.subscribe(ShowErrorEvent,controller)
            event_observer.subscribe(ControllerShowViewEvent,controller)
            event_observer.subscribe(RunControllerEvent,controller)

            home_controller_id=event_observer.get_id_by_name('home')
            event_observer.notify(MakeControllerInactiveEvent(id=home_controller_id))

            error_controller_id=controller.get_event_subscribtion_id()
            event_observer.notify(RunControllerEvent(id=error_controller_id,data={}))
            event_observer.notify(ControllerShowViewEvent(id=error_controller_id))
            return
        else:
            event_observer.notify(GotErrorEvent(self._event_subscribtion_id,error_message='Got unhandled event type {event}'))
    def get_event_subscribtion_id(self)->int:
        return self._event_subscribtion_id

