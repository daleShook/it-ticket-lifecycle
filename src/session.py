import uuid
import datetime
import random

def mock_session_timestamp(base_time=None, min_delta=5, max_delta=30):
    """
    Generate a mock timestamp by adding a random delta (in minutes)
    to a base_time or current time if not provided.
    """
    if base_time is None:
        base_time = datetime.datetime.now()
    delta = datetime.timedelta(minutes=random.randint(min_delta, max_delta))
    return base_time + delta


class Session:
    def __init__(self):
        self.session_id = str(uuid.uuid4())
        self.start_time = mock_session_timestamp()
        self.end_time = None
        self.active_tickets = []
        self.status = "Active"
        print(f"[{self.start_time.strftime('%Y-%m-%d %H:%M:%S')}] Session Started: ID: {self.session_id}")

    def add_ticket(self, ticket):
        ticket['submitted_at'] = mock_session_timestamp(self.start_time, 1, 2)
        self.active_tickets.append(ticket)
        print(f"Ticket Added: Ticket ID: {ticket['ticket_id']}")

    def close_session(self):
        self.end_time = mock_session_timestamp(self.start_time, 10, 60)
        self.status = "Complete"
        duration = self.end_time - self.start_time
        print(f"[{self.end_time.strftime('%Y-%m-%d %H:%M:%S')}] Session Ended: ID: {self.session_id}")
        print(f"Total Tickets Processed: {len(self.active_tickets)}")
        print(f"[Meta] Total Sessions: 1, Active: 0, Total Tickets: {len(self.active_tickets)}")

        # 🆕 Add total time to resolution meta
        total_minutes = int(duration.total_seconds() // 60)
        hours, minutes = divmod(total_minutes, 60)
        if hours:
            print(f"[Meta] Total Time to Resolution: {hours} hour(s) {minutes} minute(s)")
        else:
            print(f"[Meta] Total Time to Resolution: {minutes} minute(s)")
