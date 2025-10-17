
from core.Controller import Controller
from views.TodayExchangeRatesController.TodayExchangeRatesIndexView import TodayExchanegRatesIndexView


def create_TodayExchangeRatesController_data()->dict:
    return {}


# class TodayExchangeRatesController:
class TodayExchangeRatesController(Controller):
    def __init__(self,data:dict):
        super().__init__()
        
    def index(self):
        #check if data is the cache
        #if yes
        #   get data and add into view
        #if no
        #   send request to the api
        #   if return success message
        #       create view with this data
        #   if error
        #       create error page
        self._window=TodayExchanegRatesIndexView()