
from datetime import datetime, timedelta

# Sample Users
users = [
    {"user_id": 1, "name": "Rahul", "department": "HR"},
    {"user_id": 2, "name": "Sneha", "department": "Finance"},
    {"user_id": 3, "name": "Arjun", "department": "Development"}
]

# Sample Technicians
technicians = [
    {"technician_id": 1, "name": "Amit", "specialization": "Hardware"},
    {"technician_id": 2, "name": "Priya", "specialization": "Networking"},
    {"technician_id": 3, "name": "Kiran", "specialization": "Software"},
    {"technician_id": 4, "name": "Meera", "specialization": "Security"}
]

# Problem Categories
categories = ["Hardware", "Software", "Networking", "Security"]

# Default Priorities
priorities = ["Low", "Medium", "High", "Critical"]

# Ticket Status
statuses = ["Pending", "In Progress", "Resolved"]

# Sample Tickets
tickets = [
    {
        "ticket_id": 101,
        "user_id": 1,
        "category": "Networking",
        "issue": "Server is down",
        "priority": "Critical",
        "technician": "Priya",
        "status": "Pending",
        "created_at": datetime.now() - timedelta(days=2),
        "resolved_at": None
    },
    {
        "ticket_id": 102,
        "user_id": 2,
        "category": "Hardware",
        "issue": "Keyboard not working",
        "priority": "Low",
        "technician": "Amit",
        "status": "In Progress",
        "created_at": datetime.now() - timedelta(days=1),
        "resolved_at": None
    },
    {
        "ticket_id": 103,
        "user_id": 3,
        "category": "Software",
        "issue": "Software installation required",
        "priority": "Medium",
        "technician": "Kiran",
        "status": "Resolved",
        "created_at": datetime.now() - timedelta(days=3),
        "resolved_at": datetime.now() - timedelta(days=3) + timedelta(hours=2)
    }
]
