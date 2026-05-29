data = {
    "users": [
        {
            "id": 1,
            "name": "Nikita",
            "age": 19,
            "is_active": True,
            "contacts": {
                "email": "nikita@example.com",
                "phone": "+380991112233"
            },
            "orders": [
                {
                    "id": 101,
                    "status": "paid",
                    "items": [
                        {"title": "Keyboard", "price": 1200, "qty": 1},
                        {"title": "Mouse", "price": 600, "qty": 2}
                    ]
                },
                {
                    "id": 102,
                    "status": "pending",
                    "items": [
                        {"title": "Monitor", "price": 7000, "qty": 1}
                    ]
                }
            ]
        },
        {
            "id": 2,
            "name": "Anna",
            "age": 22,
            "is_active": False,
            "contacts": {
                "email": "anna@example.com"
            },
            "orders": [
                {
                    "id": 103,
                    "status": "paid",
                    "items": [
                        {"title": "Laptop", "price": 30000, "qty": 1},
                        {"title": "USB Cable", "price": 200, "qty": 3}
                    ]
                }
            ]
        },
        {
            "id": 3,
            "name": "Oleh",
            "age": 17,
            "is_active": True,
            "contacts": {},
            "orders": []
        }
    ],
    "settings": {
        "currency": "UAH",
        "discounts": {
            "student": 0.1,
            "vip": 0.2
        }
    }
}

# function №1 (get name of users)
def get_user_names(data):
    return [user["name"] for user in data["users"]]

# function №2 (get name: email)
def get_user_email(data):
    return {user["name"]: user["contacts"].get("email") or "No email" for user in data["users"]}

# function №3 (get active users)
def get_active_users(data):
    return [user["name"] for user in data["users"] if user["is_active"]]

# function №4 (get adult users)
def get_adult_users(data):
    return [user["name"] for user in data["users"] if user["age"] >= 18]   

# function №5 (count users)
def count_users(data):
    return len(data["users"])

# function №6 (count orders)
def count_user_orders(data):
    return {user["name"]: len(user["orders"]) for user in data["users"]}

print(get_user_names(data))
print(get_user_email(data))
print(get_active_users(data))
print(get_adult_users(data))
print(count_users(data))
print(count_user_orders(data))