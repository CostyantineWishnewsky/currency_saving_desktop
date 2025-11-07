
from dataclasses import dataclass
 
@dataclass
class RegisterNewItemEvent:
    name:str
    id:int
