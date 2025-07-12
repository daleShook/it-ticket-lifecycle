class Meta:
    def __init__(self):
        self.total_sessions = 0
        self.total_tickets = 0
        self.active_sessions = 0

    def start_session(self):
        self.total_sessions += 1
        self.active_sessions += 1
        print(f"[Meta] Total Sessions: {self.total_sessions}, Active: {self.active_sessions}")

    def end_session(self, ticket_count):
        self.active_sessions -= 1
        self.total_tickets += ticket_count
        print(f"[Meta] Tickets Processed: {self.total_tickets}")

    def report(self):
        return {
            "total_sessions": self.total_sessions,
            "active_sessions": self.active_sessions,
            "total_tickets": self.total_tickets
        }
