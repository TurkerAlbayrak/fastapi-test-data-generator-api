import requests

response = requests.get(
    "http://localhost:8000/api/v1/users",
    params={"count": 5, "locale": "tr_TR"}
)

users = response.json()

for user in users:
    print(f"✅ {user['first_name']} {user['last_name']} - {user['email']}")
    print(user)