
from views.TodayExchangeRatesController.TodayExchangeRatesIndexView import TodayExchanegRatesIndexView


def create_TodayExchangeRatesController_data()->dict:
    return {}


class TodayExchangeRatesController:
    def __init__(self,data:dict):
        self._window=None
        
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

    def show(self)->None:
        self._window.show()