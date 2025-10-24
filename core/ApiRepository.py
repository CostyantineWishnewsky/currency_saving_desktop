
from abc import ABC,abstractmethod

from models.ExchangeRate import ExchangeRate

class ApiRepository(ABC):

    @abstractmethod
    def get_today_exchange_rates(self)->list[ExchangeRate]:
        pass