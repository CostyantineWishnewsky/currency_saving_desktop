
from core.Controller import Controller

from core.EventObserver import EventObserver
from core.Events.ControllerCreator.GotErrorEvent import GotErrorEvent

from views.TodayExchangeRatesController.TodayExchangeRatesIndexView import TodayExchanegRatesIndexView

def create_TodayExchangeRatesController_data(id:int)->dict:
    return {'id':id}


class TodayExchangeRatesController(Controller):
    def __init__(self,data:dict):
        super().__init__(data['id'])

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
            self._window=TodayExchanegRatesIndexView(exchange_rates)
        except Exception as e:
            event_observer=EventObserver()

            error_handling_id=event_observer.get_id_by_name('error_handling')

            event_observer.notify(GotErrorEvent(error_handling_id,e))
            return