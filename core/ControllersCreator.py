

from core.patterns.SingletonMeta import SingletonMeta
from core.EventObserver import EventObserver

# from core.Events.CreateControllerEvent import CreateControllerEvent
from core.Events.CreateHomeControllerEvent import CreateHomeControllerEvent
from core.Events.GotErrorEvent import GotErrorEvent
from core.Events.ControllerShowViewEvent import ControllerShowViewEvent

from controllers.TodayExchangeRatesController import create_TodayExchangeRatesController_data, TodayExchangeRatesController

class ControllersCreator(metaclass=SingletonMeta):
# class ControllersCreator(IEventObserverSubscriable):
    def __init__(self) -> None:
        # event_observer=EventObserver()
        pass
        # event_observer.subscribe(CreateHomeControllerEvent,self)
        # event_observer.subscribe(GotErrorEvent,self)

    # def __del__(self)->None:
    #     event_observer=EventObserver()

    #     # event_observer.unsubscribe(CreateHomeControllerEvent,self)
    #     # event_observer.unsubscribe(GotErrorEvent,self)
    #     #unsubsribe from all events
    #     pass
    
    def handle_event(self,event)->None:
        print('Controller creator')
        event_observer=EventObserver()
        print('event observer has been created')
        # if type(event) ==  CreateHomeControllerEvent:
        #     print('Here in if')
        #     data=create_TodayExchangeRatesController_data()
        #     controller=TodayExchangeRatesController(data)
        #     event_observer.subscribe(ControllerShowViewEvent,controller)
        #     print('controller should be subsribed')
        #     # controller.show()
        #     #event_observer.subscribe(ControllerShowViewEvent,controller)

        #     return
        data=create_TodayExchangeRatesController_data()
        controller=TodayExchangeRatesController(data)
        event_observer.subscribe(ControllerShowViewEvent,controller)
        print('controller should be subsribed')
        # controller.show()
        #event_observer.subscribe(ControllerShowViewEvent,controller)
        
            
        #event create new controller
        #1 create controller
        #2 subsribe it on controller name and events
        #3 trigger show controller view

        return

