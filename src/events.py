class EventEmitter:
    def __init__(self):
        self.listeners = {}

    def on(self, event_name, handler):
        """Subscribe a handler function to an event."""
        if event_name not in self.listeners:
            self.listeners[event_name] = []
        self.listeners[event_name].append(handler)
        print(f"[Event Subscribed] {handler.__name__} to '{event_name}'")

    def emit(self, event_name, *args, **kwargs):
        """Trigger all handlers associated with an event."""
        if event_name in self.listeners:
            print(f"[Event Emitted] {event_name}")
            for handler in self.listeners[event_name]:
                handler(*args, **kwargs)
        else:
            print(f"[No Listeners] for event: {event_name}")
