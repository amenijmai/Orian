from clients.email_client import create_email_client
from clients.calendar_client import create_calendar_client
from clients.crm_client import create_crm_client
from memory import MemoryStore
import outils
import prompts
from config import Config
import time

class OrionAgent:
    def __init__(self):
        self.email = create_email_client()
        self.calendar = create_calendar_client()
        self.crm = create_crm_client()
        self.memory = MemoryStore()

    def run_once(self):
        """Run one polling & processing cycle."""
        actions = []
        unread = self.email.fetch_unread()

        for msg in unread:
            sid = msg['id']
            sender = msg['from']
            subject = msg.get('subject', '')
            body = msg.get('body', '')

            summary = outils.simple_summarize(body)
            intent = outils.detect_intent(subject, body)

            # Save to memory
            self.memory.append_interaction(sender, {
                'id': sid,
                'subject': subject,
                'summary': summary,
                'intent': intent,
                'date': msg.get('date')
            })

            # Log to CRM
            self.crm.log_interaction(sender, f"Email received: {summary}")
            actions.append(f"logged {sid} to CRM")

            # Handle scheduling
            if intent == 'schedule':
                event = self.calendar.create_event(
                    '2025-10-27T15:00:00Z',
                    '2025-10-27T15:30:00Z',
                    subject,
                    [sender]
                )
                self.email.send(
                    sender,
                    f"Re: {subject}",
                    f"Thanks — I proposed {event['start']} for a 30-min call. "
                    "If that doesn't work, please suggest alternatives."
                )
                actions.append(f"proposed meeting to {sender}")
            else:
                reply = self._draft_reply(subject, body, sender)
                self.email.send(sender, f"Re: {subject}", reply)
                actions.append(f"sent reply to {sender}")

        return actions

    def _draft_reply(self, subject, body, sender):
        summary = outils.simple_summarize(body, max_chars=200)
        return (
            f"Hi,\n\n"
            f"Thanks for reaching out. I received your message: \"{summary}\"\n\n"
            f"I'll follow up shortly with next steps.\n\n"
            f"Best regards,\nOrion"
        )
