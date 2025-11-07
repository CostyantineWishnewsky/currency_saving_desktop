from dataclasses import dataclass
 
@dataclass
class GotErrorEvent:
    id:int 
    error_message:str
