import requests


BASE_URL = "https://jsonplaceholder.typicode.com/todos"


# ==========================================
# 1. CREATE
# ==========================================

new_todo = {
    "userId": 1,
    "title": "Complete Module 4",
    "completed": False
}

response = requests.post(
    BASE_URL,
    json=new_todo
)

print("=== CREATE ===")
print("POST /todos")
print(f"Status Code: {response.status_code}")

created_todo = response.json()

print(f"Created todo: {created_todo}")
print()

todo_id = created_todo["id"]


# ==========================================
# 2. READ
# ==========================================

response = requests.get(
    f"{BASE_URL}/{todo_id}"
)

print("=== READ ===")
print(f"GET /todos/{todo_id}")
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    todo = response.json()
    print(f"Todo found: {todo}")
else:
    print(
        "Todo was not found. "
        "JSONPlaceholder does not permanently save POST requests."
    )

print()


# ==========================================
# 3. UPDATE
# ==========================================

update_data = {
    "completed": True
}

response = requests.patch(
    f"{BASE_URL}/{todo_id}",
    json=update_data
)

print("=== UPDATE ===")
print(f"PATCH /todos/{todo_id}")
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    updated_todo = response.json()
    print(f"Todo updated: {updated_todo}")
else:
    print("Update could not be verified on the fake API.")

print()


# ==========================================
# 4. READ AGAIN
# ==========================================

response = requests.get(
    f"{BASE_URL}/{todo_id}"
)

print("=== READ AGAIN ===")
print(f"GET /todos/{todo_id}")
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    todo = response.json()
    print(f"Todo after update: {todo}")
else:
    print(
        "Todo was not found because JSONPlaceholder "
        "does not persist changes."
    )

print()


# ==========================================
# 5. DELETE
# ==========================================

response = requests.delete(
    f"{BASE_URL}/{todo_id}"
)

print("=== DELETE ===")
print(f"DELETE /todos/{todo_id}")
print(f"Status Code: {response.status_code}")

if response.status_code in [200, 204]:
    print("Delete request accepted.")
else:
    print("Delete request was not successful.")

print()


# ==========================================
# 6. VERIFY DELETE
# ==========================================

response = requests.get(
    f"{BASE_URL}/{todo_id}"
)

print("=== VERIFY DELETE ===")
print(f"GET /todos/{todo_id}")
print(f"Status Code: {response.status_code}")

if response.status_code == 404:
    print("Todo is not found.")
elif response.status_code == 200:
    print(
        "Todo still appears because JSONPlaceholder "
        "is a fake API and does not persist changes."
    )
else:
    print("Unexpected response.")