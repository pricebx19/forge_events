"""Forge Events package for event-driven architecture.

This package provides a powerful event system for the Forge framework.
"""

from forge_events.service import EventService, EventSubscriber, IEventSubscriber

__all__ = ["EventService", "EventSubscriber", "IEventSubscriber"]

__version__ = "0.1.0" 