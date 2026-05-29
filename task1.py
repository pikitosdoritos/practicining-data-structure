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
    dict_of_emails = {}

    for user in data["users"]:
        user_email = user["contacts"].get("email")
        user_name = user["name"]

        if user_email:
            dict_of_emails[user_name] = user_email
        else:
            dict_of_emails[user_name] = "No email"

    return dict_of_emails

print(get_user_names(data))
print(get_user_email(data))