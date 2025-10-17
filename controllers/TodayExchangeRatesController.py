
from core.Controller import Controller
from core.CacheRepository import CacheRepository

from views.TodayExchangeRatesController.TodayExchangeRatesIndexView import TodayExchanegRatesIndexView

def create_TodayExchangeRatesController_data()->dict:
    return {}


class TodayExchangeRatesController(Controller):
    def __init__(self,data:dict,cache_repository:CacheRepository):
        super().__init__()
        self._cache_repository=cache_repository
        
    def index(self):
        if self._cache_repository.is_setupped()==False:
            self._cache_repository.setup()
        if self._cache_repository.is_table_updated_today('exchange_rates'):
            exchange_rates=self._cache_repository.get_all_exchange_rates()
            self._window=TodayExchanegRatesIndexView(exchange_rates)
        #if no
        #   send request to the api
        #   if return success message
        #       create view with this data
        #   if error
        #       create error page
        #Here should be api
        self._window=TodayExchanegRatesIndexView([])