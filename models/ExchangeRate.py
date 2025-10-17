
from dataclasses import dataclass

from models.Currency import Currency
from models.SourceOfInformation import SourceOfInformation


@dataclass
class ExchangeRate:
    id:int
    currency_from:Currency
    currency_to:Currency
    value:int 
    #replace if for multiplier
    amount_of_numbers_after_point:int
    source_of_information:SourceOfInformation
    #created_at