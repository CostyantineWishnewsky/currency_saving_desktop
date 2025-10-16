
from views.TodayExchangeRatesController.TodayExchangeRatesIndexView import TodayExchanegRatesIndexView

class TodayExchangeRatesController:
    def __init__(self):
        self.window=None
        
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
        self.window=TodayExchanegRatesIndexView()