
import sys

from PySide6.QtWidgets import QApplication

from core.patterns.SingletonMeta import SingletonMeta

from __globals import CACH_REPOSITORY

from controllers.TodayExchangeRatesController import TodayExchangeRatesController
from controllers.ErrorController import ErrorController

class EventSystem(metaclass=SingletonMeta):
    def __init__(self):
        self._application=QApplication(sys.argv)
        self._controllers={}
        self._last_index=0
        self._is_running=False

    def trigger_event_create_controller(self,route:str,data:dict)->int:
        if route == "home":
            controller=TodayExchangeRatesController(data,CACH_REPOSITORY)
            controller.index()
        elif route == 'error':
            controller=ErrorController(data)
            controller.index()
        else:
            raise Exception(f"No such route as {route}")

        new_index=self._last_index+1
        self._controllers[new_index]=controller

        self._last_index=new_index

        return self._last_index

    
    def trigger_event_delete_controller(self,index:int)->None:
        #Raises KeyError if controller with index not found
        del self._controllers[index]
            
        

    def trigger_event_make_controller_active(self,index:int)->None:
        #Raises KeyError if controller with index not found
        self._controllers[index].make_active()
        

    def trigger_event_make_controller_inactive(self,index:int)->None:
        #Raises KeyError if controller with index not found
        self._controllers[index].make_inactive()
    
    def trigger_event_stop_application(self,index:int)->None:
        if self._is_running==False:
            raise("Cannot stop not running application")
        self._app.quit()

    def run(self)->None:
        if self._is_running==True:
            raise Exception("Cannot run application twice")
        for controller in self._controllers.values():
            controller.show()
        
        self._is_running=True
        self._application.exec()