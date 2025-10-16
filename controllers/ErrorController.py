
from views.statuses.ErrorView import ErrorView

def create_ErrorController_data(error_message:str)->dict:
    return {'error_message':error_message}

class ErrorController:
    def __init__(self,data:dict):
        self._window=None
        self._error_message=data['error_message']
    def index(self):
        self._window=ErrorView(error_message=self._error_message)
        
    def set_error_message(self,error_message:str)->None:
        self._error_message=error_message

    def show(self)->None:
        self._window.show()