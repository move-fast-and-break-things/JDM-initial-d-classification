class EventHandler():
    __slots__ = ('event_types')

    def __init__(self, depends):
        self.depends= depends
        self.event_types=[]
        self.initate()
    
    def initate(self):
        pass

    async def check_event(self,event):
        '''This method check event'''
        pass

    async def handle_event(self,event):
        pass

    def get_event_types(self):
        return self.event_types
