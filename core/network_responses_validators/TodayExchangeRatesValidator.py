
import json

from decimal import Decimal

from models.ExchangeRate import ExchangeRate
from models.Currency import Currency
from models.SourceOfInformation import SourceOfInformation

class TodayExchangeRatesValidator:
    def __init__(self,json_string:str) -> None:
        self._json_string=json_string
        self._date_item_supposed_fields={
            "currency_from":str,
            "currency_to":str,
            "value":str,
            "source":str,
        }

        self._exchange_rate_id=0
        self._currency_id=0

    #It could raise an exception
    def get_validated(self)->list[ExchangeRate]:
        #TODO should validation of /api/v1/currency-info/today/ json response

        response_dict=json.loads(self._json_string)

        exchange_rates=[]
        sources_of_information={}
        currencies={}
        
        #check header
        if response_dict["header"]["result"] != "ok":
            print('it is not ok')
            #TODO raise Exception with error message from response_dict data if it exists
            pass


        #check data
        for date_item in response_dict["data"]:
            for key  in date_item.keys():
                if key not in self._date_item_supposed_fields.keys():
                    #TODO Error key not found
                    break
                if type(date_item[key])!=self._date_item_supposed_fields[key]:
                    #TODO Got Error here
                    break
                
            if date_item.keys()!=self._date_item_supposed_fields.keys():
                #TODO error
                continue

            
            if date_item["currency_from"] not in currencies.keys():
               currencies[date_item["currency_from"]]=Currency(id=self._currency_id,name=date_item["currency_from"])
               self._currency_id=self._currency_id+1

            if date_item["currency_to"] not in currencies.keys():
                currencies[date_item["currency_to"]]=Currency(id=self._currency_id,name=date_item["currency_to"])
                self._currency_id=self._currency_id+1
            #TODO make checking if it can be converted into Decimal
            value=Decimal(date_item["value"])


            if date_item["source"] not in sources_of_information:
                sources_of_information[date_item["source"]]=SourceOfInformation(id=0,name=date_item["source"])
            
            
            exchange_rates.append(ExchangeRate(id=self._exchange_rate_id,currency_from=currencies[date_item["currency_from"]],currency_to=currencies[date_item["currency_to"]],value=value,source_of_information=sources_of_information[date_item["source"]]))
            self._exchange_rate_id=self._exchange_rate_id+1
        return exchange_rates