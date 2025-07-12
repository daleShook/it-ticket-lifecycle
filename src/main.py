from src.session import Session
from src.workflow import Workflow
from src.meta import Meta

meta = Meta()

def main():
    print_banner()

    # Start session and increment meta
    session = Session()
    meta.start_session()

    # --- User Input: Name ---
    while True:
        user_name = input("Enter your name: ").strip()
        if user_name:
            break
        print("[Error] Name cannot be empty. Please enter your name.")

    # --- User Input: Issue Description ---
    while True:
        issue_type = input("Describe your issue: ").strip()
        if issue_type:
            break
        print("[Error] Issue description required. Please try again.")

    # Initialize workflow with session
    workflow = Workflow(session)

    # Run full workflow
    workflow.run_workflow(user_name, issue_type)

    # End session and update meta
    session.close_session()
    meta.end_session(ticket_count=len(session.active_tickets))

    # Report system stats
    print_meta_summary(meta)


def print_banner():
    print("===============================")
    print(" IT Ticket Lifecycle Simulator ")
    print("===============================")


def print_meta_summary(meta):
    stats = meta.report()
    print(f"[Meta] Total Sessions: {stats['total_sessions']}, "
          f"Active: {stats['active_sessions']}, "
          f"Total Tickets: {stats['total_tickets']}")
    print("===============================")
    print("    Session Complete ✅        ")
    print("===============================")


if __name__ == "__main__":
    main()
