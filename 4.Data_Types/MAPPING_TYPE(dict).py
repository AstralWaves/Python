print("=== Python Data Types Tutorial ===")


# 🗂 MAPPING TYPE: dict
# Stores key-value pairs, with unique keys.
print("\n=== dict ===")
user = {"name": "Alex", "age": 25}

print(f"Dict: {user}")  # Output: {'name': 'Alex', 'age': 25}
print(f"Name: {user['name']}")  # Output: Alex

user["city"] = "Berlin"  # Add key-value pair
print(f"Updated: {user}")  # Output: {'name': 'Alex', 'age': 25, 'city': 'Berlin'}