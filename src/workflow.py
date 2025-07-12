import random
import datetime
from src.events import EventEmitter


def mock_timestamp(base_time=None, min_delta=1, max_delta=5):
    """
    Generate a mock timestamp by adding a random delta (in minutes)
    to a base_time or current time if not provided.
    """
    if base_time is None:
        base_time = datetime.datetime.now()
    delta = datetime.timedelta(minutes=random.randint(min_delta, max_delta))
    return base_time + delta


class Workflow:
    def __init__(self, session):
        self.session = session
        self.event_emitter = EventEmitter()

        self.event_emitter.on("ticket_escalated", self.handle_escalation)
        self.event_emitter.on("ticket_resolved", self.handle_resolution)

    def submit_ticket(self, user_name, issue_type):
        timestamp = mock_timestamp()
        ticket = {
            "ticket_id": random.randint(1000, 9999),
            "user_name": user_name,
            "issue_type": issue_type,
            "priority_level": random.choice(["Low", "Medium", "High"]),
            "assigned_team": None,
            "status": "Open",
            "submitted_at": timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }
        print(f"[{ticket['submitted_at']}] Ticket Submitted: {ticket}")
        self.session.add_ticket(ticket)
        return ticket

    def categorize_ticket(self, ticket):
        timestamp = mock_timestamp()
        print(f"[{timestamp.strftime('%Y-%m-%d %H:%M:%S')}] Categorize Ticket: Priority: {ticket['priority_level']}")
        if ticket["priority_level"] == "High":
            self.event_emitter.emit("ticket_escalated", ticket)

    def assign_ticket(self, ticket):
        timestamp = mock_timestamp()
        teams = ["Help Desk", "Network Ops", "SysAdmin"]
        ticket["assigned_team"] = random.choice(teams)
        print(f"[{timestamp.strftime('%Y-%m-%d %H:%M:%S')}] Ticket Assigned: Assigned to {ticket['assigned_team']}")

    def resolve_ticket(self, ticket):
        timestamp = mock_timestamp()
        ticket["status"] = "Resolved"
        print(f"[{timestamp.strftime('%Y-%m-%d %H:%M:%S')}] Ticket Resolved: Ticket ID: {ticket['ticket_id']}")
        self.event_emitter.emit("ticket_resolved", ticket)

    def notify_user(self, ticket):
        timestamp = mock_timestamp()
        print(f"[{timestamp.strftime('%Y-%m-%d %H:%M:%S')}] Notify User: Ticket {ticket['ticket_id']} resolved. "
              f"Notification sent to {ticket['user_name']}.")

    def handle_escalation(self, ticket):
        timestamp = mock_timestamp()
        print(f"[{timestamp.strftime('%Y-%m-%d %H:%M:%S')}] Escalation: Ticket {ticket['ticket_id']} has been escalated!")

    def handle_resolution(self, ticket):
        timestamp = mock_timestamp()
        print(f"[{timestamp.strftime('%Y-%m-%d %H:%M:%S')}] Resolution Handler: Post-resolution tasks for "
              f"Ticket {ticket['ticket_id']}.")

    def run_workflow(self, user_name, issue_type):
        ticket = self.submit_ticket(user_name, issue_type)
        self.categorize_ticket(ticket)
        self.assign_ticket(ticket)
        self.resolve_ticket(ticket)
        self.notify_user(ticket)
