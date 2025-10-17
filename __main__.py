

from core.EventSystem import EventSystem
from controllers.TodayExchangeRatesController import create_TodayExchangeRatesController_data

def main()->None:
    event_system=EventSystem()
    event_system.setup()
    
    data=create_TodayExchangeRatesController_data()
    event_system.trigger_event_create_controller("home",data=data)

    event_system.run()


if __name__ == "__main__":
    main()