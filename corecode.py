from datetime import datetime, timedelta

# ==========================================
#        IT HELP DESK TRACKER
#        PHASE 1 - PROCEDURAL PROGRAMMING
# ==========================================

# Sample Users
users = [
    {"user_id": 1, "name": "Rahul", "department": "HR"},
    {"user_id": 2, "name": "Sneha", "department": "Finance"},
    {"user_id": 3, "name": "Arjun", "department": "Development"}
]

# Sample Technicians
technicians = [
    {"technician_id": "T01", "name": "Amit", "specialization": "Hardware"},
    {"technician_id": "T02", "name": "Priya", "specialization": "Networking"},
    {"technician_id": "T03", "name": "Kiran", "specialization": "Software"}
]

# Sample Tickets
now = datetime.now()

tickets = [
    {
        "ticket_id": 101,
        "user_id": 1,
        "issue": "Server is down",
        "priority": "Critical",
        "technician": "Priya",
        "status": "Pending",
        "created_at": now - timedelta(days=2),
        "resolved_at": None
    },
    {
        "ticket_id": 102,
        "user_id": 2,
        "issue": "Keyboard not working",
        "priority": "Low",
        "technician": "Amit",
        "status": "In Progress",
        "created_at": now - timedelta(days=1),
        "resolved_at": None
    },
    {
        "ticket_id": 103,
        "user_id": 3,
        "issue": "Software installation required",
        "priority": "Medium",
        "technician": "Kiran",
        "status": "Resolved",
        "created_at": now - timedelta(days=3),
        "resolved_at": now - timedelta(days=3) + timedelta(hours=2)
    }
]

priorities = ["Low", "Medium", "High", "Critical"]
statuses = ["Pending", "In Progress", "Resolved"]

# ==========================================
# 1. REGISTER USER
# ==========================================

def register_user():
    print("\n--- REGISTER USER ---")

    name = input("Enter user name: ").strip()
    department = input("Enter department: ").strip()

    if not name or not department:
        print("Name and department cannot be empty.")
        return

    user_id = max([u["user_id"] for u in users], default=0) + 1

    users.append({
        "user_id": user_id,
        "name": name,
        "department": department
    })

    print("User registered successfully!")
    print("User ID:", user_id)

# ==========================================
# 2. AUTOMATIC PRIORITY ASSIGNMENT
# ==========================================

def determine_priority(issue):

    issue = issue.lower()

    critical_keywords = [
        "server down",
        "system crash",
        "data loss",
        "security breach"
    ]

    high_keywords = [
        "internet",
        "network",
        "not starting",
        "not working",
        "system failure"
    ]

    medium_keywords = [
        "software",
        "installation",
        "login",
        "password",
        "application"
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

    return "Low"

# ==========================================
# 3. CREATE NEW TICKET
# ==========================================

def create_ticket():

    print("\n--- CREATE NEW TICKET ---")

    if not users:
        print("No users registered. Register a user first.")
        return

    print("\nRegistered Users:")

    for user in users:
        print(user["user_id"], "-", user["name"])

    user_input = input("\nEnter User ID: ").strip()

    if not user_input.isdigit():
        print("Invalid User ID.")
        return

    user_id = int(user_input)

    user = next(
        (u for u in users if u["user_id"] == user_id),
        None
    )

    if user is None:
        print("User not found.")
        return

    issue = input("Enter technical issue: ").strip()

    if not issue:
        print("Issue description cannot be empty.")
        return

    # Automatically determine priority
    priority = determine_priority(issue)

    ticket_id = max(
        [t["ticket_id"] for t in tickets],
        default=100
    ) + 1

    ticket = {
        "ticket_id": ticket_id,
        "user_id": user_id,
        "issue": issue,
        "priority": priority,
        "technician": "Not Assigned",
        "status": "Pending",
        "created_at": datetime.now(),
        "resolved_at": None
    }

    tickets.append(ticket)

    print("\nTicket created successfully!")
    print("Ticket ID:", ticket_id)
    print("Issue:", issue)
    print("Automatically Assigned Priority:", priority)
    print("Status: Pending")

# ==========================================
# 4. VIEW ALL TICKETS
# ==========================================

def view_all_tickets():

    print("\n--- ALL TICKETS ---")

    if not tickets:
        print("No tickets available.")
        return

    for ticket in tickets:

        user = next(
            (u for u in users if u["user_id"] == ticket["user_id"]),
            None
        )

        user_name = user["name"] if user else "Unknown"

        print("\nTicket ID:", ticket["ticket_id"])
        print("User:", user_name)
        print("Issue:", ticket["issue"])
        print("Priority:", ticket["priority"])
        print("Technician:", ticket["technician"])
        print("Status:", ticket["status"])
        print("Created At:", ticket["created_at"].strftime("%d-%m-%Y %H:%M"))

# ==========================================
# 5. SEARCH TICKET
# ==========================================

def search_ticket():

    print("\n--- SEARCH TICKET ---")

    ticket_input = input("Enter Ticket ID: ").strip()

    if not ticket_input.isdigit():
        print("Invalid Ticket ID.")
        return

    ticket_id = int(ticket_input)

    for ticket in tickets:

        if ticket["ticket_id"] == ticket_id:

            print("\nTicket Found!")
            print("Ticket ID:", ticket["ticket_id"])
            print("User ID:", ticket["user_id"])
            print("Issue:", ticket["issue"])
            print("Priority:", ticket["priority"])
            print("Technician:", ticket["technician"])
            print("Status:", ticket["status"])
            print("Created At:", ticket["created_at"])

            return

    print("Ticket not found.")

# ==========================================
# 6. MANUAL PRIORITY CHANGE
# ==========================================

def change_priority():

    print("\n--- CHANGE TICKET PRIORITY ---")

    ticket_input = input("Enter Ticket ID: ").strip()

    if not ticket_input.isdigit():
        print("Invalid Ticket ID.")
        return

    ticket_id = int(ticket_input)

    for ticket in tickets:

        if ticket["ticket_id"] == ticket_id:

            print("\nCurrent Priority:", ticket["priority"])

            print("\nAvailable Priorities:")

            for i, priority in enumerate(priorities, 1):
                print(i, ".", priority)

            choice = input("Select new priority (1-4): ").strip()

            if choice not in ["1", "2", "3", "4"]:
                print("Invalid priority choice.")
                return

            ticket["priority"] = priorities[int(choice) - 1]

            print("Priority changed successfully!")
            print("New Priority:", ticket["priority"])

            return

    print("Ticket not found.")

# ==========================================
# 7. ASSIGN TECHNICIAN
# ==========================================

def assign_technician():

    print("\n--- ASSIGN TECHNICIAN ---")

    ticket_input = input("Enter Ticket ID: ").strip()

    if not ticket_input.isdigit():
        print("Invalid Ticket ID.")
        return

    ticket_id = int(ticket_input)

    for ticket in tickets:

        if ticket["ticket_id"] == ticket_id:

            print("\nAvailable Technicians:")

            for tech in technicians:
                print(
                    tech["technician_id"],
                    "-",
                    tech["name"],
                    "(" + tech["specialization"] + ")"
                )

            tech_id = input("\nEnter Technician ID: ").strip().upper()

            for tech in technicians:

                if tech["technician_id"] == tech_id:

                    ticket["technician"] = tech["name"]

                    print("Technician assigned successfully!")
                    print("Assigned Technician:", tech["name"])

                    return

            print("Technician not found.")
            return

    print("Ticket not found.")

# ==========================================
# 8. UPDATE TICKET STATUS
# ==========================================

def update_ticket_status():

    print("\n--- UPDATE TICKET STATUS ---")

    ticket_input = input("Enter Ticket ID: ").strip()

    if not ticket_input.isdigit():
        print("Invalid Ticket ID.")
        return

    ticket_id = int(ticket_input)

    for ticket in tickets:

        if ticket["ticket_id"] == ticket_id:

            print("\nAvailable Status:")

            for i, status in enumerate(statuses, 1):
                print(i, ".", status)

            choice = input("Select status (1-3): ").strip()

            if choice not in ["1", "2", "3"]:
                print("Invalid status choice.")
                return

            new_status = statuses[int(choice) - 1]

            if ticket["status"] == "Resolved":
                print("This ticket is already resolved.")
                return

            if new_status == "Resolved":
                ticket["resolved_at"] = datetime.now()

            ticket["status"] = new_status

            print("Ticket status updated successfully!")
            print("New Status:", new_status)

            return

    print("Ticket not found.")

# ==========================================
# 9. VIEW PENDING TICKETS
# ==========================================

def view_pending_tickets():

    print("\n--- PENDING TICKETS ---")

    found = False

    for ticket in tickets:

        if ticket["status"] in ["Pending", "In Progress"]:

            found = True

            print("\nTicket ID:", ticket["ticket_id"])
            print("Issue:", ticket["issue"])
            print("Priority:", ticket["priority"])
            print("Technician:", ticket["technician"])
            print("Status:", ticket["status"])

    if not found:
        print("No pending tickets available.")

# ==========================================
# 10. VIEW RESOLVED TICKETS
# ==========================================

def view_resolved_tickets():

    print("\n--- RESOLVED TICKETS ---")

    found = False

    for ticket in tickets:

        if ticket["status"] == "Resolved":

            found = True

            print("\nTicket ID:", ticket["ticket_id"])
            print("Issue:", ticket["issue"])
            print("Technician:", ticket["technician"])
            print("Resolved At:", ticket["resolved_at"])

    if not found:
        print("No resolved tickets available.")

# ==========================================
# 11. CALCULATE RESOLUTION TIME
# ==========================================

def calculate_resolution_time():

    print("\n--- RESOLUTION TIME ---")

    ticket_input = input("Enter Ticket ID: ").strip()

    if not ticket_input.isdigit():
        print("Invalid Ticket ID.")
        return

    ticket_id = int(ticket_input)

    for ticket in tickets:

        if ticket["ticket_id"] == ticket_id:

            if ticket["status"] != "Resolved":
                print("This ticket has not been resolved yet.")
                return

            duration = ticket["resolved_at"] - ticket["created_at"]

            total_seconds = int(duration.total_seconds())

            days = total_seconds // 86400
            hours = (total_seconds % 86400) // 3600
            minutes = (total_seconds % 3600) // 60

            print("\nTicket ID:", ticket_id)
            print("Issue:", ticket["issue"])
            print(
                "Resolution Time:",
                days, "days,",
                hours, "hours and",
                minutes, "minutes"
            )

            return

    print("Ticket not found.")

# ==========================================
# 12. GENERATE TICKET SUMMARY
# ==========================================

def generate_summary():

    print("\n--- TICKET SUMMARY ---")

    total = len(tickets)

    pending = sum(
        1 for t in tickets if t["status"] == "Pending"
    )

    in_progress = sum(
        1 for t in tickets if t["status"] == "In Progress"
    )

    resolved = sum(
        1 for t in tickets if t["status"] == "Resolved"
    )

    print("\nTotal Tickets:", total)
    print("Pending Tickets:", pending)
    print("In Progress Tickets:", in_progress)
    print("Resolved Tickets:", resolved)

    print("\n--- PRIORITY SUMMARY ---")

    for priority in priorities:

        count = sum(
            1 for t in tickets if t["priority"] == priority
        )

        print(priority, ":", count)

# ==========================================
# 13. MAIN MENU
# ==========================================

def main():

    while True:

        print("\n========================================")
        print("          IT HELP DESK TRACKER")
        print("========================================")

        print("1. Register User")
        print("2. Create New Ticket")
        print("3. View All Tickets")
        print("4. Search Ticket")
        print("5. Change Ticket Priority")
        print("6. Assign Technician")
        print("7. Update Ticket Status")
        print("8. View Pending Tickets")
        print("9. View Resolved Tickets")
        print("10. Calculate Resolution Time")
        print("11. Generate Ticket Summary")
        print("12. Exit")

        print("========================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_user()

        elif choice == "2":
            create_ticket()

        elif choice == "3":
            view_all_tickets()

        elif choice == "4":
            search_ticket()

        elif choice == "5":
            change_priority()

        elif choice == "6":
            assign_technician()

        elif choice == "7":
            update_ticket_status()

        elif choice == "8":
            view_pending_tickets()

        elif choice == "9":
            view_resolved_tickets()

        elif choice == "10":
            calculate_resolution_time()

        elif choice == "11":
            generate_summary()

        elif choice == "12":
            print("\nThank you for using IT Help Desk Tracker!")
            break

        else:
            print("Invalid choice! Please select between 1 and 12.")

# ==========================================
# PROGRAM EXECUTION
# ==========================================

main()
