
from core.Controller import Controller

from views.TodayExchangeRatesController.TodayExchangeRatesIndexView import TodayExchanegRatesIndexView
from views.statuses.ErrorView import ErrorView

def create_TodayExchangeRatesController_data()->dict:
    return {}


class TodayExchangeRatesController(Controller):
    def __init__(self,data:dict):
        super().__init__()

    def index(self):
        try:
            if self._cache_repository.is_setupped()==False:
                self._cache_repository.setup()
            if self._cache_repository.is_table_updated_today('exchange_rates'):
                exchange_rates=self._cache_repository.get_all_exchange_rates()
                self._window=TodayExchanegRatesIndexView(exchange_rates)
                return
            exchange_rates=self._api_repository.get_today_exchange_rates()
            self._cache_repository.update_exchange_rates(exchange_rates)
            #if no
            #   send request to the api
            #   if return success message
            #       create view with this data
            #   if error
            #       create error page
            #Here should be api
            # self._window=TodayExchanegRatesIndexView([])
            # exchange_rates=self._cache_repository.get_all_exchange_rates()
            self._window=TodayExchanegRatesIndexView(exchange_rates)
        except ConnectionRefusedError as e:
            # print("Connection refused.")
            self._window=ErrorView(error_message=e)

        #TODO handle Not Found
        #TODO handle Invalid Request
        #TODO handle Server Not Found
        #TODO handle Server Forbidden
        #TODO handle other Exception