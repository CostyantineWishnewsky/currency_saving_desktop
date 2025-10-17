
import json
from datetime import date
import os
from datetime import date

from core.CacheRepository import CacheRepository

from models.ExchangeRate import ExchangeRate
from models.SourceOfInformation import SourceOfInformation
from models.Currency import Currency

from formats import DAY_TIME_FORMAT


class JsonCacheRepository(CacheRepository):
    def __init__(self,path:str):
        self._path=path

        self._db_schema={
            "header":{
                "updated":{
                    "exchange_rates":"",
                }
            },
            "data":{
                "exchange_rates":{

                }
            }
        }


    def setup(self)->None:
        try:
            database=self._db_schema
            
            database["header"]["updated"]["exchange_rates"]=date.today().strftime(DAY_TIME_FORMAT)
            with open(self._path,'w') as f:
                json.dump(database, f)
        except Exception as e:
            #TODO here
            pass
    
    def is_setupped(self)->bool:
        #TODO make openning with cheking structure
        return os.path.isfile(self._path)
        

    def is_table_updated_today(self,table_name:str)->bool:
        with open(self._path,'r') as f:
            data=json.load(f)
        
        if table_name in data["header"]["updated"].keys():
            today_date=date.today().strftime(DAY_TIME_FORMAT)
            if data["header"]["updated"][table_name] == today_date:
                return True
            return False
        raise Exception(f"No such table as {table_name}")


    def get_all_exchange_rates(self)->list[ExchangeRate]:
        #TODO try here
        with open(self._path,'r') as f:
            data=json.load(f)
        exchange_rates=[]
        for item in data["data"]["exchange_rates"]:
            currency_from=Currency(id=item["currency_from"]["id"],name=item["currency_from"]["name"])
            currency_to=Currency(id=item["currency_to"]["id"],name=item["currency_to"]["name"])
            source_of_information=SourceOfInformation(id=item["source_of_information"]["id"],name=item["source_of_information"]["name"])

            exchange_rate=ExchangeRate(id=item["id"],currency_from=currency_from,currency_to=currency_to,value=item["value"],multiplier=item["multiplier"],source_of_information=source_of_information)
            exchange_rates.append(exchange_rate)
        return exchange_rates
        

    def update_exchange_rates(self,updated_exchange_rates:list[ExchangeRate])->None:
        #TODO try here
        with open(self._path,'r') as f:
            data=json.load(f)
        exchange_rates=data["data"]["exchange_rates"]

        #Inserting into exchange_rates
        for exchange_rate in updated_exchange_rates:
            exchange_rate_dict={'id':exchange_rate.id,'currency_from':{'id':exchange_rate.currency_from.id,'name':exchange_rate.currency_from.name},'currency_to':{'id':exchange_rate.currency_to.id,'name':exchange_rate.currency_to.name},'value':exchange_rate.value,'multiplier':exchange_rate.multiplier,'source_of_information':{'id':exchange_rate.source_of_information.id,'name':exchange_rate.source_of_information.name}}
            exchange_rates.append(exchange_rate_dict)

        data["data"]["exchange_rates"]=exchange_rates
        with open(self._path,'w') as f:
            json.dump(data,f)
        