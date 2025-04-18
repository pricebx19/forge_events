# Forge Events

An event-driven architecture package for the Forge framework.

## Features

- Event publishing and subscribing
- Priority-based event handling
- Asynchronous event processing
- Integration with the Forge framework

## Installation

```bash
pip install forge_events
```

## Usage

```python
from forge_events import EventService, EventSubscriber

# Create an event service
event_service = EventService()

# Subscribe to an event
@event_service.subscribe("user.created", priority=10)
async def handle_user_created(user_data):
    print(f"User created: {user_data['name']}")

# Publish an event
await event_service.publish("user.created", {"id": 1, "name": "John Doe"})
```

## Event Subscribers

Event subscribers are callables that receive event data when an event is published. They are registered with the event service and are invoked when an event is published.

```python
# Register with a decorator
@event_service.subscribe("application.starting")
async def on_app_starting(app):
    print("Application is starting")

# Or register with the subscribe method
def handle_app_stopping(app):
    print("Application is stopping")

subscriber = event_service.subscribe("application.stopping", handle_app_stopping)

# Unsubscribe if needed
event_service.unsubscribe(subscriber)
```

## Priority

Event subscribers can be registered with a priority. Higher priority subscribers are invoked first.

```python
@event_service.subscribe("user.deleted", priority=100)
async def high_priority_handler(user_data):
    print("High priority handler")

@event_service.subscribe("user.deleted", priority=50)
async def medium_priority_handler(user_data):
    print("Medium priority handler")

@event_service.subscribe("user.deleted", priority=10)
async def low_priority_handler(user_data):
    print("Low priority handler")
```

## Integration with Forge

Forge Core automatically integrates with Forge Events when both are installed:

```python
from forge_core import App

app = App()

@app.on_event("request.received")
async def log_request(request):
    print(f"Request received: {request.method} {request.path}")

@app.on_event("request.completed", priority=10)
async def log_response(data):
    print(f"Response: {data['response'].status}")
```

## License

MIT
