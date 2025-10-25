
from http.client import HTTPConnection
import json

from core.ApiRepository import ApiRepository
from core.network_responses_validators.TodayExchangeRatesValidator import TodayExchangeRatesValidator

from models.ExchangeRate import ExchangeRate

class HttpApiRepository(ApiRepository):
    def __init__(self,host:str,port:int):
        self._host=host
        self._port=port
        self._headers={
                        "Content-type": "application/json",
                        "Host": self._host,
                    }
        self._default_sources=[
            "google.com",
            "mockup-bank.com",
        ]
    
    def get_today_exchange_rates(self)->list[ExchangeRate]:
        url="/api/v1/currency-info/today/"
        request_data={
            "sources":self._default_sources
        }

        json_request_data = json.dumps(request_data)
        connection=HTTPConnection(self._host,self._port)

        #TODO check if connection is established
        connection.request("POST", url=url,body=json_request_data,headers=self._headers)
        #TODO check if got response if not raise error
        response = connection.getresponse()
    
        validator=TodayExchangeRatesValidator(response.read().decode('utf-8'))
        connection.close()
        return validator.get_validated()