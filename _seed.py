
from __globals import CACH_REPOSITORY

from models.ExchangeRate import ExchangeRate
from models.Currency import Currency
from models.SourceOfInformation import SourceOfInformation


def seed():
    currencies={
        "usd":Currency(1,"usd"),
        "euro":Currency(2,"euro"),
        "uah":Currency(3,"uah")
    }

    sources_of_information={
        "google.com":SourceOfInformation(1,"google.com"),
        "mockup-bank1":SourceOfInformation(2,"mockup-bank1"),
        "mockup-bank2":SourceOfInformation(3,"mockup-bank2"),
    }

    exchange_rates=[]
    current_currency_name="usd"
    id_counter=0
    for currency_name in currencies.keys():
        for currency in currencies.values():
            if currency_name == currency.name:
                continue
            for source_of_information in sources_of_information.values():
                exchange_rate=ExchangeRate(id=id_counter,currency_from=currencies[currency_name],currency_to=currency,value=12,source_of_information=source_of_information)
                exchange_rates.append(exchange_rate)
                id_counter+=1
                
    CACH_REPOSITORY.update_exchange_rates(exchange_rates)
    print('Success')

    

if __name__ == "__main__":
    seed()