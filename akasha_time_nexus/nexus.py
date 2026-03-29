from __future__ import annotations

from .enrichers import (
    build_clock_context,
    build_lunar_context,
    build_solar_context,
    build_weather_context,
)
from .models import ContextBundle, EnrichedEvent, EventInput


class TimeNexus:
    def __init__(self, timezone_name: str = "UTC") -> None:
        self.timezone_name = timezone_name

    def stamp(self, event: EventInput) -> EnrichedEvent:
        clock = build_clock_context(event.timestamp_utc, timezone_name=self.timezone_name)
        solar = build_solar_context(event.timestamp_utc, event.latitude, event.longitude, timezone_name=self.timezone_name)
        lunar = build_lunar_context(event.timestamp_utc, event.latitude, event.longitude)
        weather = build_weather_context(event.timestamp_utc, event.latitude, event.longitude)

        bundle = ContextBundle(
            clock=clock,
            solar=solar,
            lunar=lunar,
            weather=weather,
            extra={},
        )
        return EnrichedEvent(event=event, context=bundle)


def stamp_event(
    timestamp_utc: str,
    latitude: float,
    longitude: float,
    event_type: str = "observation",
    title: str = "",
    notes: str = "",
    source: str = "manual",
    metadata: dict | None = None,
    timezone_name: str = "UTC",
) -> EnrichedEvent:
    nexus = TimeNexus(timezone_name=timezone_name)
    event = EventInput(
        timestamp_utc=timestamp_utc,
        latitude=latitude,
        longitude=longitude,
        event_type=event_type,
        title=title,
        notes=notes,
        source=source,
        metadata=metadata or {},
    )
    return nexus.stamp(event)
