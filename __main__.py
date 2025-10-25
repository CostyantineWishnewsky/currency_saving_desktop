


from core.EventObserver import EventObserver

from core.Events.CreateHomeControllerEvent import CreateHomeControllerEvent
from core.Events.ControllerShowViewEvent import ControllerShowViewEvent

from core.ControllersCreator import ControllersCreator

def main()->None:
    event_observer=EventObserver()
    event_observer.setup()

    controllers_creator=ControllersCreator()

    event_observer.subscribe(CreateHomeControllerEvent,controllers_creator)
    event_observer.subscribe(ControllerShowViewEvent,controllers_creator)

    event_observer.notify(CreateHomeControllerEvent)
    event_observer.notify(ControllerShowViewEvent('home'))

    event_observer.run()


if __name__ == "__main__":
    main()