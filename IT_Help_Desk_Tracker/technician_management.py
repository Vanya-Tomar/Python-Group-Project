from data import tickets, technicians


# ==========================================
# 1. ASSIGN TECHNICIAN
# ==========================================

def assign_technician():

    print("\n========== ASSIGN TECHNICIAN ==========")

    try:
        ticket_id = int(input("Enter Ticket ID: "))

    except ValueError:
        print("Invalid Ticket ID.")
        return

    ticket = None

    for t in tickets:
        if t["ticket_id"] == ticket_id:
            ticket = t
            break

    if ticket is None:
        print("Ticket not found.")
        return

    if ticket["status"] == "Resolved":
        print("Cannot assign a technician to a resolved ticket.")
        return

    print("\nAvailable Technicians:")

    for technician in technicians:
        print(
            technician["technician_id"],
            "-",
            technician["name"],
            "(" + technician["specialization"] + ")"
        )

    try:
        technician_id = int(input("\nSelect Technician ID: "))

    except ValueError:
        print("Invalid Technician ID.")
        return

    selected_technician = None

    for technician in technicians:
        if technician["technician_id"] == technician_id:
            selected_technician = technician
            break

    if selected_technician is None:
        print("Technician not found.")
        return

    # Assign technician to ticket
    ticket["technician"] = selected_technician["name"]

    print("\nTechnician assigned successfully!")
    print("Ticket ID:", ticket_id)
    print("Assigned Technician:", selected_technician["name"])


# ==========================================
# 2. VIEW TECHNICIAN WORKLOAD
# ==========================================

def view_technician_workload():

    print("\n========== TECHNICIAN WORKLOAD ==========")

    for technician in technicians:

        assigned_tickets = []

        for ticket in tickets:

            if (
                ticket["technician"] == technician["name"]
                and ticket["status"] != "Resolved"
            ):
                assigned_tickets.append(ticket)

        print("\nTechnician:", technician["name"])
        print("Specialization:", technician["specialization"])
        print("Active Tickets:", len(assigned_tickets))

        if assigned_tickets:

            print("Assigned Ticket IDs:")

            for ticket in assigned_tickets:
                print(
                    ticket["ticket_id"],
                    "-",
                    ticket["issue"],
                    "(" + ticket["status"] + ")"
                )

        else:
            print("No active tickets.")

