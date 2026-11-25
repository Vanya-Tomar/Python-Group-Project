from data import users


# Register New User
def register_user():

    print("\n========== USER REGISTRATION ==========")

    name = input("Enter user name: ").strip()
    department = input("Enter department: ").strip()

    if name == "" or department == "":
        print("Name and department cannot be empty.")
        return

    user_id = max([u["user_id"] for u in users], default=0) + 1

    users.append({
        "user_id": user_id,
        "name": name,
        "department": department
    })

    print("\nUser registered successfully!")
    print("User ID:", user_id)