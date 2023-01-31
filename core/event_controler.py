from core.event_types import EventTypes


class EventControler():
    def __init__(self,handlers, depends):
        self.handlers = handlers
        self.depends = depends

    async def processing(self, event):
        for handler in self.handlers:
            handler = handler(self.depends)
            if self.__check_event_type(handler,event) and await handler.check_event(event) : 
                await handler.handle_event(event)
                return
        
    def __check_event_type(self, handler, event):
        list_events = handler.get_event_types()

        for a in list_events:
            if isinstance(a, EventTypes) and event.get(a.value, False):
                return True
        return False
