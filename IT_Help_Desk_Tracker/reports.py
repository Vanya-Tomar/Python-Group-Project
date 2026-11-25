from data import tickets, priorities, categories


# ==========================================
# 1. VIEW PENDING TICKETS
# ==========================================

def view_pending_tickets():

    print("\n========== PENDING TICKETS ==========")

    pending = []

    for ticket in tickets:
        if ticket["status"] == "Pending":
            pending.append(ticket)

    if not pending:
        print("No pending tickets.")
        return

    for ticket in pending:

        print("\nTicket ID:", ticket["ticket_id"])
        print("Category:", ticket["category"])
        print("Issue:", ticket["issue"])
        print("Priority:", ticket["priority"])
        print("Technician:", ticket["technician"] or "Not Assigned")
        print("Estimated Resolution Time:",
              ticket.get("estimated_resolution", "Not available"))
        print("Status:", ticket["status"])
        print("--------------------------------")


# ==========================================
# 2. VIEW RESOLVED TICKETS
# ==========================================

def view_resolved_tickets():

    print("\n========== RESOLVED TICKETS ==========")

    resolved = []

    for ticket in tickets:
        if ticket["status"] == "Resolved":
            resolved.append(ticket)

    if not resolved:
        print("No resolved tickets.")
        return

    for ticket in resolved:

        print("\nTicket ID:", ticket["ticket_id"])
        print("Category:", ticket["category"])
        print("Issue:", ticket["issue"])
        print("Priority:", ticket["priority"])
        print("Technician:", ticket["technician"] or "Not Assigned")
        print("Estimated Resolution Time:",
              ticket.get("estimated_resolution", "Not available"))
        print("Created At:", ticket["created_at"])
        print("Resolved At:", ticket["resolved_at"])
        print("--------------------------------")


# ==========================================
# 3. CALCULATE ACTUAL RESOLUTION TIME
# ==========================================

def calculate_resolution_time():

    print("\n========== RESOLUTION TIME ==========")

    try:
        ticket_id = int(input("Enter Ticket ID: "))

    except ValueError:
        print("Invalid Ticket ID.")
        return

    for ticket in tickets:

        if ticket["ticket_id"] == ticket_id:

            if ticket["status"] != "Resolved":
                print("This ticket is not yet resolved.")
                return

            if ticket["resolved_at"] is None:
                print("Resolution time is not available.")
                return

            resolution_time = (
                ticket["resolved_at"] - ticket["created_at"]
            )

            total_seconds = int(resolution_time.total_seconds())

            days = total_seconds // 86400
            hours = (total_seconds % 86400) // 3600
            minutes = (total_seconds % 3600) // 60

            print("\nTicket ID:", ticket_id)
            print("Actual Resolution Time:")
            print(days, "Days", hours, "Hours", minutes, "Minutes")

            return

    print("Ticket not found.")


# ==========================================
# 4. GENERATE TICKET SUMMARY
# ==========================================

def generate_summary():

    print("\n========== TICKET SUMMARY ==========")

    total = len(tickets)

    pending = 0
    in_progress = 0
    resolved = 0

    for ticket in tickets:

        if ticket["status"] == "Pending":
            pending += 1

        elif ticket["status"] == "In Progress":
            in_progress += 1

        elif ticket["status"] == "Resolved":
            resolved += 1

    print("\nTotal Tickets:", total)
    print("Pending Tickets:", pending)
    print("In Progress Tickets:", in_progress)
    print("Resolved Tickets:", resolved)

    print("\nPriority Summary:")

    for priority in priorities:

        count = 0

        for ticket in tickets:
            if ticket["priority"] == priority:
                count += 1

        print(priority, ":", count)


# ==========================================
# 5. VIEW TICKETS BY CATEGORY
# ==========================================

def view_tickets_by_category():

    print("\n========== TICKETS BY CATEGORY ==========")

    for category in categories:

        category_tickets = []

        for ticket in tickets:

            if ticket["category"] == category:
                category_tickets.append(ticket)

        print("\nCategory:", category)
        print("Total Tickets:", len(category_tickets))

        if category_tickets:

            for ticket in category_tickets:

                print(
                    "Ticket ID:", ticket["ticket_id"],
                    "| Issue:", ticket["issue"],
                    "| Priority:", ticket["priority"],
                    "| Estimated Resolution:",
                    ticket.get("estimated_resolution", "Not available"),
                    "| Status:", ticket["status"]
                )

        else:
            print("No tickets in this category.")
