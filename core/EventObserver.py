
import sys

from PySide6.QtWidgets import QApplication

from core.patterns.SingletonMeta import SingletonMeta
from core.UIData import UIData

# from core.ControllersCreator import ControllersCreator
# from __globals import CONTROLLERS_CREATOR

# from controllers.TodayExchangeRatesController import TodayExchangeRatesController
# from controllers.ErrorController import ErrorController

class EventObserver(metaclass=SingletonMeta):
    def __init__(self):
        self._application=QApplication(sys.argv)
        self._event_subscribers={}
        # self._controllers={}
        # self._last_index=0
        self._is_running=False

    def setup(self)->None:
        palette=self._application.palette()
        ui_data=UIData()
        ui_data.set_pallete(palette)

        # self.subscribe('create_home_controller',CONTROLLERS_CREATOR)

    def notify(self,event)->None:
        print('here should be notification')
        if type(event) in self._event_subscribers.keys():
            for subscriber in self._event_subscribers[type(event)]:
                subscriber.handle_event(event)
            # self._event_subscribers[type(event)].handle_event(event)
            return
        #TODO here should be raise
        
        pass

    def subscribe(self,event_type,event_subscriber)->None:
        if event_type not in self._event_subscribers.keys():
            self._event_subscribers[event_type]=[event_subscriber]
            return
        self._event_subscribers[event_type].append(event_subscriber)

    def unsubscribe(self,event_type,event_subscriber)->None:
        if event_type not in self._event_subscribers.keys():
            raise Exception(f"There is no subsribtion of {event_subscriber} on {event_type} event")
        # for subscriber in self._event_subscribers[event]:
        #     if subscriber == event_subscriber
        for i in range(len(self._event_subscribers[event_type])):
            if self._event_subscribers[event_type][i] == event_subscriber:
                del self._event_subscribers[event_type][i]
                return
        raise Exception(f"There is no subsribtion of {event_subscriber} on {event_type} event")
        
    # def trigger_event_create_controller(self,route:str,data:dict)->int:
    #     if route == "home":
    #         controller=TodayExchangeRatesController(data)
    #         controller.index()
    #     elif route == 'error':
    #         controller=ErrorController(data)
    #         controller.index()
    #     else:
    #         raise Exception(f"No such route as {route}")

    #     new_index=self._last_index+1
    #     self._controllers[new_index]=controller

    #     self._last_index=new_index

    #     return self._last_index

    
    # def trigger_event_delete_controller(self,index:int)->None:
    #     #TODO Raises KeyError if controller with index not found
    #     del self._controllers[index]
            
        

    # def trigger_event_make_controller_active(self,index:int)->None:
    #     #TODO Raises KeyError if controller with index not found
    #     self._controllers[index].make_active()
        

    # def trigger_event_make_controller_inactive(self,index:int)->None:
    #     #TODO Raises KeyError if controller with index not found
    #     self._controllers[index].make_inactive()
    
    # def trigger_event_stop_application(self,index:int)->None:
    #     if self._is_running==False:
    #         raise("Cannot stop not running application")
    #     self._app.quit()

    def run(self)->None:
        if self._is_running==True:
            raise Exception("Cannot run application twice")
        
        # self._event_subscribers['home_controller']
        # for controller in self._controllers.values():
        #     controller.show()
        
        self._is_running=True
        self._application.exec()