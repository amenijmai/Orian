from typing import List, Dict
from datetime import datetime
from config import Config

class BaseEmailClient:
    def fetch_unread(self) -> List[Dict]:
        raise NotImplementedError

    def send(self, to: str, subject: str, body: str, in_reply_to: str = None):
        raise NotImplementedError


class MockEmailClient(BaseEmailClient):
    def __init__(self):
        self._inbox = [
            {
                'id': 'm1',
                'from': 'alice@acme.com',
                'subject': 'Quick call about the proposal',
                'body': "Hi, can we schedule a call next week to discuss the proposal?",
                'date': datetime.utcnow().isoformat(),
            },
            {
                'id': 'm2',
                'from': 'billing@vendor.com',
                'subject': 'Invoice #12345',
                'body': 'Attached invoice for September.',
                'date': datetime.utcnow().isoformat(),
            },
        ]

    def fetch_unread(self):
        items = self._inbox[:]
        self._inbox = []
        return items

    def send(self, to, subject, body, in_reply_to=None):
        print(f"[MockEmail] Sending to={to} subject={subject}\n{body}\n---")
        return True


def create_email_client():
    provider = Config.EMAIL_PROVIDER
    if provider == 'mock':
        return MockEmailClient()
    raise NotImplementedError('Only mock provider implemented in this scaffold')
