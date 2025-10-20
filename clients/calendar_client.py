from typing import Dict, Any
from config import Config

class BaseCalendarClient:
    def create_event(self, start, end, title, attendees):
        raise NotImplementedError


class MockCalendarClient(BaseCalendarClient):
    def create_event(self, start, end, title, attendees):
        print(f"[MockCalendar] Created event '{title}' {start} - {end} attendees={attendees}")
        return {'id': 'ev1', 'start': start, 'end': end, 'title': title}


def create_calendar_client():
    if Config.CALENDAR_PROVIDER == 'mock':
        return MockCalendarClient()
    raise NotImplementedError('Only mock provider implemented')
