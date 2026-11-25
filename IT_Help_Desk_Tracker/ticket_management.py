from datetime import datetime

from data import users, tickets, priorities, statuses, categories


# ==========================================
#       AUTOMATIC PRIORITY ASSIGNMENT
# ==========================================

def determine_priority(category, issue):

    issue = issue.lower()

    critical_keywords = [
        "server down",
        "system crash",
        "data loss",
        "security breach",
        "unauthorized access",
        "hacked"
    ]

    high_keywords = [
        "not starting",
        "system failure",
        "network failure",
        "internet not working",
        "entire system",
        "complete system failure"
    ]

    medium_keywords = [
        "software error",
        "application error",
        "login problem",
        "installation problem",
        "application not opening"
    ]

    for word in critical_keywords:
        if word in issue:
            return "Critical"

    for word in high_keywords:
        if word in issue:
            return "High"

    for word in medium_keywords:
        if word in issue:
            return "Medium"

    # Default priority based on category

    category_priority = {
        "Hardware": "Low",
        "Software": "Medium",
        "Networking": "High",
        "Security": "Critical"
    }

    return category_priority.get(category, "Low")


# ==========================================
#       ESTIMATED RESOLUTION TIME
# ==========================================

def get_estimated_resolution(priority):

    estimated_times = {
        "Critical": 2,
        "High": 8,
        "Medium": 24,
        "Low": 48
    }

    total_hours = estimated_times[priority]

    days = total_hours // 24
    hours = total_hours % 24

    if days > 0 and hours > 0:
        return f"{days} days {hours} hours"

    elif days > 0:
        return f"{days} days"

    else:
        return f"{hours} hours"


# ==========================================
#              CREATE TICKET
# ==========================================

def create_ticket():

    print("\n========== CREATE NEW TICKET ==========")

    user_id = input("Enter User ID: ")

    user = None

    for u in users:
        if str(u["user_id"]) == user_id:
            user = u
            break

    if user is None:
        print("User not found!")
        return

    print("\nAvailable Categories:")

    for i, category in enumerate(categories, start=1):
        print(i, ".", category)

    try:
        choice = int(input("Select Category: "))

        if choice < 1 or choice > len(categories):
            print("Invalid category choice!")
            return

    except ValueError:
        print("Please enter a valid number!")
        return

    category = categories[choice - 1]

    issue = input("Enter Problem Description: ").strip()

    if issue == "":
        print("Problem description cannot be empty!")
        return

    # Automatically determine priority

    priority = determine_priority(category, issue)

    # Calculate estimated resolution time

    estimated_time = get_estimated_resolution(priority)

    # Generate ticket ID

    if len(tickets) == 0:
        ticket_id = 101
    else:
        ticket_id = max(t["ticket_id"] for t in tickets) + 1

    # Create ticket

    ticket = {
        "ticket_id": ticket_id,
        "user_id": user_id,
        "category": category,
        "issue": issue,
        "priority": priority,
        "technician": None,
        "status": "Pending",
        "created_at": datetime.now(),
        "resolved_at": None,
        "estimated_resolution": estimated_time
    }

    tickets.append(ticket)

    print("\nTicket Created Successfully!")
    print("--------------------------------")
    print("Ticket ID:", ticket_id)
    print("User:", user["name"])
    print("Category:", category)
    print("Issue:", issue)
    print("Automatically Assigned Priority:", priority)
    print("Estimated Resolution Time:", estimated_time)
    print("Status: Pending")
    print("--------------------------------")


# ==========================================
#             VIEW ALL TICKETS
# ==========================================

def view_all_tickets():

    print("\n========== ALL TICKETS ==========")

    if len(tickets) == 0:
        print("No tickets available!")
        return

    for ticket in tickets:

        print("\nTicket ID:", ticket["ticket_id"])
        print("User ID:", ticket["user_id"])
        print("Category:", ticket["category"])
        print("Issue:", ticket["issue"])
        print("Priority:", ticket["priority"])
        print("Technician:", ticket["technician"])
        print("Status:", ticket["status"])
        print("Estimated Resolution Time:",
              ticket.get("estimated_resolution", "Not available"))
        print("Created At:", ticket["created_at"])

        print("--------------------------------")


# ==========================================
#              SEARCH TICKET
# ==========================================

def search_ticket():

    print("\n========== SEARCH TICKET ==========")

    try:
        ticket_id = int(input("Enter Ticket ID: "))

    except ValueError:
        print("Please enter a valid Ticket ID!")
        return

    for ticket in tickets:

        if ticket["ticket_id"] == ticket_id:

            print("\nTicket Found!")
            print("--------------------------------")
            print("Ticket ID:", ticket["ticket_id"])
            print("User ID:", ticket["user_id"])
            print("Category:", ticket["category"])
            print("Issue:", ticket["issue"])
            print("Priority:", ticket["priority"])
            print("Technician:", ticket["technician"])
            print("Status:", ticket["status"])
            print("Estimated Resolution Time:",
                  ticket.get("estimated_resolution", "Not available"))
            print("Created At:", ticket["created_at"])

            print("--------------------------------")
            return

    print("Ticket not found!")


# ==========================================
#          UPDATE TICKET STATUS
# ==========================================

def update_ticket_status():

    print("\n========== UPDATE TICKET STATUS ==========")

    try:
        ticket_id = int(input("Enter Ticket ID: "))

    except ValueError:
        print("Please enter a valid Ticket ID!")
        return

    for ticket in tickets:

        if ticket["ticket_id"] == ticket_id:

            print("\nCurrent Status:", ticket["status"])

            print("\nAvailable Statuses:")

            for i, status in enumerate(statuses, start=1):
                print(i, ".", status)

            try:
                choice = int(input("Select New Status: "))

                if choice < 1 or choice > len(statuses):
                    print("Invalid status choice!")
                    return

            except ValueError:
                print("Please enter a valid number!")
                return

            new_status = statuses[choice - 1]

            ticket["status"] = new_status

            if new_status == "Resolved":
                ticket["resolved_at"] = datetime.now()

            print("\nTicket Status Updated Successfully!")
            print("New Status:", new_status)

            return

    print("Ticket not found!")