
from dataclasses import dataclass

from models.Currency import Currency
from models.SourceOfInformation import SourceOfInformation

from decimal import Decimal

@dataclass
class ExchangeRate:
    id:int
    currency_from:Currency
    currency_to:Currency
    value:Decimal
    source_of_information:SourceOfInformation
