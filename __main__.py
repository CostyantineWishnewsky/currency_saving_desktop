


from core.EventObserver import EventObserver

from core.Events.ControllerCreator.CreateHomeControllerEvent import CreateHomeControllerEvent
from core.Events.Controller.RunControllerEvent import RunControllerEvent

from core.ControllersCreator import ControllersCreator

def main()->None:
    event_observer=EventObserver()
    event_observer.setup()

    id=event_observer.get_last_event_subscriber_id()

    controllers_creator=ControllersCreator(id)
    controllers_creator.setup()

    controllers_creator_id=controllers_creator.get_event_subscribtion_id()
    event_observer.notify(CreateHomeControllerEvent(controllers_creator_id))


    home_controller_id=event_observer.get_id_by_name('home')

    event_observer.notify(RunControllerEvent(id=home_controller_id,data={}))
    event_observer.run()


if __name__ == "__main__":
    main()
