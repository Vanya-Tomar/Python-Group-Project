from user_management import register_user

from ticket_management import (
    create_ticket,
    view_all_tickets,
    search_ticket,
    update_ticket_status
)

from technician_management import (
    assign_technician,
    view_technician_workload
)

from reports import (
    view_pending_tickets,
    view_resolved_tickets,
    calculate_resolution_time,
    generate_summary,
    view_tickets_by_category
)


# ==========================================
#        IT HELP DESK TRACKER
# ==========================================

def main():

    while True:

        print("\n")
        print("==========================================")
        print("          IT HELP DESK TRACKER")
        print("==========================================")

        print("\n1. Register User")
        print("2. Create New Ticket")
        print("3. View All Tickets")
        print("4. Search Ticket")
        print("5. Assign Technician")
        print("6. Update Ticket Status")
        print("7. View Pending Tickets")
        print("8. View Resolved Tickets")
        print("9. Calculate Resolution Time")
        print("10. Generate Ticket Summary")
        print("11. View Tickets by Category")
        print("12. View Technician Workload")
        print("13. Exit")

        print("\n==========================================")

        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            print("\nInvalid input! Please enter a number.")
            continue

        if choice == 1:
            register_user()

        elif choice == 2:
            create_ticket()

        elif choice == 3:
            view_all_tickets()

        elif choice == 4:
            search_ticket()

        elif choice == 5:
            assign_technician()

        elif choice == 6:
            update_ticket_status()

        elif choice == 7:
            view_pending_tickets()

        elif choice == 8:
            view_resolved_tickets()

        elif choice == 9:
            calculate_resolution_time()

        elif choice == 10:
            generate_summary()

        elif choice == 11:
            view_tickets_by_category()

        elif choice == 12:
            view_technician_workload()

        elif choice == 13:
            print("\nThank you for using IT Help Desk Tracker!")
            break

        else:
            print("\nInvalid choice! Please select between 1 and 13.")


# ==========================================
# RUN THE PROGRAM
# ==========================================

if __name__ == "__main__":
    main()